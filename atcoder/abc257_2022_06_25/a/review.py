"""A - A to Z String 2
問題文
A を N 個、B を N 個、…、Z を N 個この順に繋げて得られる文字列の先頭から X 番目の文字を求めてください。

解説

N = 2, X = 12 の場合を考える。
このとき考える文字列は下記のとおり。
AABB...ZZ
これは下記の数列とみなすことができる。
0, 0, 1, 1, ..., 25, 25
各要素に対し、インデックスを割り当てると下記のようになる。

インデックス(X - 1): 0, 1, 2, 3, ..., 50, 51
数列               : 0, 0, 1, 1, ..., 25, 25

インデックスを N で割って切り捨てた値の数列(以後 floor 数列)を考えると下記のようになる。

インデックス(X - 1): 0, 1, 2, 3, ..., 50, 51
数列               : 0, 0, 1, 1, ..., 25, 25
floor 数列         : 0, 0, 1, 1, ..., 25, 25

対象の数列と floor 数列は同じである。
したがって、この数列の X 番目の数は
floor((X - 1) / N)
と表される。
"""

import sys


def main():
    N, X = map(int, input().split())
    print(chr(ord('A') + (X - 1) // N).upper())


if __name__ == '__main__':
    main()
