# -*- coding : utf-8 -*-
# @Time: 2023/9/18 22:48
# @Author: yefei.wang
# @File: b.py
import sys

sys.stdin = open('input.txt', 'r')


def solve(n, m, a, b):
    orb = 0
    for i in range(m):
        orb |= b[i]
    mi = 0
    mx = 0
    for i in range(n):
        mi = min(mi ^ a[i], mi ^ (a[i] | orb))
        mx ^= a[i]
    mx |= orb
    print(mi, mx)


def main():
    tcn = int(input())
    for _ in range(tcn):
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        solve(n, m, a, b)


if __name__ == '__main__':
    main()
