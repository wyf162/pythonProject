# -*- coding : utf-8 -*-
# @Time: 2023/9/21 22:58
# @Author: yefei.wang
# @File: b.py
import sys

# sys.stdin = open('../input.txt', 'r')


def solve(n, a):
    s = 1
    for i in range(n):
        s *= a[i]
    ans = s
    for i in range(n):
        if a[i] == 0:
            t = 1
            for j in range(n):
                if i != j:
                    t *= a[j]
                else:
                    t *= (a[j] + 1)
            ans = max(ans, t)
        else:
            ans = max(ans, s * (a[i] + 1) // a[i])
    print(ans)


def main():
    tcn = int(input())
    for _ in range(tcn):
        n = int(input())
        a = list(map(int, input().split()))
        solve(n, a)


if __name__ == '__main__':
    main()
