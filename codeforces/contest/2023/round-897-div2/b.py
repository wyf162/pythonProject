# -*- coding : utf-8 -*-
# @Time: 2023/9/11 23:02
# @Author: yefei.wang
# @File: c.py
# import sys
# sys.stdin = open('input.txt', 'r')


def solve(n, s):
    diff = 0
    same = 0
    for i in range(n >> 1):
        if s[i] != s[n - i - 1]:
            diff += 1
        else:
            same += 2

    k = 2 if n % 2 == 0 else 1
    upper = diff + same + (0 if n % 2 == 0 else 1)

    rst = [0] * (n + 1)
    for i in range(diff, upper + 1, k):
        rst[i] = 1
    print(''.join(map(str, rst)))


def main():
    tcn = int(input())
    for _ in range(tcn):
        n = int(input())
        s = input()
        solve(n, s)


if __name__ == '__main__':
    main()
