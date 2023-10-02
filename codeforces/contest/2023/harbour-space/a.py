# -*- coding : utf-8 -*-
# @Time: 2023/8/26 22:38
# @Author: yefei.wang
# @File: minimumPossibleSum.py

# import sys
#
# sys.stdin = open('input.txt', 'r')


def increasing_and_decreasing(x, y, n):
    if (y - x) < (n * (n - 1)) / 2:
        print(-1)
        return
    a1, an = x, y
    td = y - x
    d1 = td - int((n - 1) * (n - 2) / 2)
    print(a1, end=' ')
    a2 = a1 + d1
    print(a2, end=' ')
    ai = a2
    for i in range(n - 2, 1, -1):
        ai = ai + i
        print(ai, end=' ')
    print(an)


def main():
    tcn = int(input())
    for _ in range(tcn):
        x, y, n = [int(x) for x in input().split()]
        increasing_and_decreasing(x, y, n)


if __name__ == '__main__':
    main()
