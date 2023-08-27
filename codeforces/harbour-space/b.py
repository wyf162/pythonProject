# -*- coding : utf-8 -*-
# @Time: 2023/8/26 22:56
# @Author: yefei.wang
# @File: b.py

# import sys
#
# sys.stdin = open('input.txt', 'r')


def swap_and_reverse(n, k, s):
    ss = list(s)
    if k % 2 == 0:
        ss.sort()
        print(''.join(ss))
    else:
        events = [ss[i] for i in range(0, n, 2)]
        odds = [ss[i] for i in range(1, n, 2)]
        events.sort()
        odds.sort()
        for i in range(0, n, 2):
            ss[i] = events[int(i / 2)]
        for i in range(1, n, 2):
            ss[i] = odds[int(i / 2)]
        print(''.join(ss))


def main():
    tcn = int(input())
    for _ in range(tcn):
        n, k = [int(x) for x in input().split()]
        s = input()
        swap_and_reverse(n, k, s)


if __name__ == '__main__':
    main()
