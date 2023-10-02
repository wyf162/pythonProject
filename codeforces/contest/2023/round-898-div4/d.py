# -*- coding : utf-8 -*-
# @Time: 2023/9/21 23:16
# @Author: yefei.wang
# @File: d.py
import sys


# sys.stdin = open('../input.txt', 'r')


def solve(n, k, s):
    i = 0
    ans = 0
    while i < n:
        if s[i] == 'B':
            i += k
            ans += 1
        else:
            i += 1
    print(ans)


def main():
    tcn = int(input())
    for _ in range(tcn):
        n, k = map(int, input().split())
        s = input()
        solve(n, k, s)


if __name__ == '__main__':
    main()
