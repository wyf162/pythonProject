# -*- coding : utf-8 -*-
# @Time: 2023/9/22 20:27
# @Author: yefei.wang
# @File: e.py
import sys

# sys.stdin = open('../input.txt', 'r')


def solve(n, x, a):
    def water(h):
        return sum(max(h - a[i], 0) for i in range(n))

    l, r = 1, 10 ** 10
    ans = 1
    while l <= r:
        m = (l + r) >> 1
        if water(m) <= x:
            ans = m
            l = m + 1
        else:
            r = m - 1
    print(ans)


def main():
    tcn = int(input())
    for _ in range(tcn):
        n, x = map(int, input().split())
        a = list(map(int, input().split()))
        solve(n, x, a)


if __name__ == '__main__':
    main()
