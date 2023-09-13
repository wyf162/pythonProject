# -*- coding : utf-8 -*-
# @Time: 2023/8/30 22:47
# @Author: yefei.wang
# @File: a.py

# import sys
#
# sys.stdin = open('input.txt', 'r')


def channel(n, a, q, ss):
    worse = a
    best = a
    offline = 0
    online = 0
    for s in ss:
        if s == '-':
            if online > 0:
                online -= 1
            else:
                offline += 1
        elif s == '+':
            if offline > 0:
                offline -= 1
            else:
                worse += 1
            best += 1

    if worse >= n:
        print('YES')
    elif best < n:
        print('NO')
    else:
        print('MAYBE')


def main():
    tcn = int(input())
    for _ in range(tcn):
        n, a, q = [int(x) for x in input().split()]
        ss = input()
        channel(n, a, q, ss)


if __name__ == '__main__':
    main()
