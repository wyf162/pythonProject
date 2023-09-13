# -*- coding : utf-8 -*-
# @Time: 2023/8/31 23:07
# @Author: yefei.wang
# @File: b.py

# import sys
#
# sys.stdin = open('input.txt', 'r')


def solve(a, b):
    n = len(a)
    if n == 2:
        print('YES')
        return
    ones, zeros, df = 0, 0, 0
    for i in range(n):
        if a[i] != b[i]:
            df += 1
        else:
            if a[i] == '1':
                if ones > 0:
                    df = 0
                    zeros = 0
                ones = 1
            else:
                if zeros > 0:
                    df = 0
                    ones = 0
                zeros = 1

    ones, zeros, rdf = 0, 0, 0
    for i in range(n-1, -1, -1):
        if a[i] != b[i]:
            rdf += 1
        else:
            if a[i] == '1':
                if ones > 0:
                    rdf = 0
                    zeros = 0
                ones = 1
            else:
                if zeros > 0:
                    rdf = 0
                    ones = 0
                zeros = 1

    if df == 0 or rdf == 0:
        print('YES')
    else:
        print('NO')


def main():
    tcn = int(input())
    for _ in range(tcn):
        a = input()
        b = input()
        solve(a, b)


if __name__ == '__main__':
    main()
