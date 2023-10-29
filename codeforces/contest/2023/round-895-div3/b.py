# -*- coding : utf-8 -*-
# @Time: 2023/9/7 23:08
# @Author: yefei.wang
# @File: c.py
# import sys

# sys.stdin = open('input.txt', 'r')


def solve(n, ds):
    rst = 400
    for d, s in ds:
        rst = min(d + (s - 1) // 2, rst)
    print(rst)


def main():
    tcn = int(input())
    for _ in range(tcn):
        n = int(input())
        ds = []
        for i in range(n):
            ds.append(list(map(int, input().split())))
        solve(n, ds)


if __name__ == '__main__':
    main()
