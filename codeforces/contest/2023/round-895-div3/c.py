# -*- coding : utf-8 -*-
# @Time: 2023/9/7 23:55
# @Author: yefei.wang
# @File: c.py
import math
# import sys

# sys.stdin = open('input.txt', 'r')


def solve(l, r):
    # print(l, r)
    if r <= 3:
        print(-1)
        return
    if r - l > 0:
        if r % 2 == 0:
            print(2, r - 2)
            return
        else:
            print(2, r - 3)
            return
    else:
        for i in range(2, math.ceil(math.sqrt(l))+1, 1):
            if l % i == 0:
                print(i, l-i)
                return
    print(-1)


def main():
    tcn = int(input())
    for _ in range(tcn):
        l, r = list(map(int, input().split(' ')))
        solve(l, r)


if __name__ == '__main__':
    main()
