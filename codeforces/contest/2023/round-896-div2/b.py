# -*- coding : utf-8 -*-
# @Time: 2023/9/10 23:00
# @Author: yefei.wang
# @File: c.py

from math import inf


# import sys

# sys.stdin = open('input.txt', 'r')


def solve(n, k, a, b, coords):
    if n == k:
        print(0)
        return
    mi_a = inf
    mi_b = inf
    rst = abs(coords[a - 1][0] - coords[b - 1][0]) + abs(coords[a - 1][1] - coords[b - 1][1])
    for i in range(k):
        tmp_a = abs(coords[a - 1][0] - coords[i][0]) + abs(coords[a - 1][1] - coords[i][1])
        if tmp_a < mi_a:
            mi_a = tmp_a

        tmp_b = abs(coords[b - 1][0] - coords[i][0]) + abs(coords[b - 1][1] - coords[i][1])
        if tmp_b < mi_b:
            mi_b = tmp_b

        if mi_a + mi_b < rst:
            rst = mi_a + mi_b
        if rst == 0:
            print(rst)
            return
    print(rst)


def main():
    tcn = int(input())
    for _ in range(tcn):
        n, k, a, b = map(int, input().split())
        coords = []
        for _i in range(n):
            coords.append(list(map(int, input().split())))
        solve(n, k, a, b, coords)


if __name__ == '__main__':
    main()
