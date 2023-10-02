# -*- coding : utf-8 -*-
# @Time: 2023/8/31 23:38
# @Author: yefei.wang
# @File: c.py

# import sys
#
# sys.stdin = open('input.txt', 'r')


def solve(s):
    k = 0
    st = -1
    unst = -1
    for a in s:
        if a == '+':
            k += 1
        elif a == '-':
            k -= 1
            if unst > -1 and unst > k:
                unst = -1
            if st > -1 and k == st - 1:
                st -= 1
        elif a == '1':
            if unst > 0 and k >= unst:
                print('NO')
                return
            else:
                st = k
        elif a == '0':
            if st > 0 and k <= st:
                print('NO')
                return
            elif k < 2:
                print('NO')
                return
            else:
                unst = k
    print('YES')


def main():
    tcn = int(input())
    for _ in range(tcn):
        s = input()
        solve(s)


if __name__ == '__main__':
    main()
