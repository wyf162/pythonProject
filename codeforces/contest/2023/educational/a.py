# -*- coding : utf-8 -*-
# @Time: 2023/8/31 22:34
# @Author: yefei.wang
# @File: a.py
# import sys
#
# sys.stdin = open('input.txt', 'r')


def solve(s):
    for a in s:
        if a == '3':
            print(37)
            return
        if a == '7':
            print(73)
            return


if __name__ == '__main__':
    tcn = int(input())
    for _ in range(tcn):
        s = input()
        solve(s)
