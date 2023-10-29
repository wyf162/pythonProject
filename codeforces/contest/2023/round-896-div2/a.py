# -*- coding : utf-8 -*-
# @Time: 2023/9/10 22:39
# @Author: yefei.wang
# @File: c.py
# import sys
# sys.stdin = open('input.txt', 'r')


def solve(n):
    if n % 2 == 0:
        print(2)
        print(1, n)
        print(1, n)
    else:
        print(4)
        print(1, n)
        print(1, n - 1)
        print(n - 1, n)
        print(1, n)


def main():
    tcn = int(input())
    for _ in range(tcn):
        n = int(input())
        input()
        solve(n)


if __name__ == '__main__':
    main()
