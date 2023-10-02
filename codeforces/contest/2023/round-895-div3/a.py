# -*- coding : utf-8 -*-
# @Time: 2023/9/7 22:34
# @Author: yefei.wang
# @File: a.py
import math
# import sys

# sys.stdin = open('input.txt', 'r')


def solve(a, b, c):
    ret = math.ceil(abs(b - a) / c / 2)
    print(ret)


def main():
    tcn = int(input())
    for _ in range(tcn):
        a, b, c = list(map(int, input().split()))
        solve(a, b, c)


if __name__ == '__main__':
    main()
