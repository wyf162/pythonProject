# -*- coding : utf-8 -*-
# @Time: 2023/8/26 23:09
# @Author: yefei.wang
# @File: c.py

# import sys
#
# sys.stdin = open('input.txt', 'r')


def divisor_chain(n):
    k = n
    bits = []
    while k > 0:
        bits.append(k % 2)
        k = k // 2
    # print(bits)
    ans = [n]
    k = n
    for i in range(len(bits)-1):
        if bits[i]:
            k = k - (1 << i)
            ans.append(k)
    for i in range(len(bits)-2, -1, -1):
        k = k - (1 << i)
        ans.append(k)
    print(len(ans))
    print(' '.join(str(x) for x in ans))


def main():
    tcn = int(input())
    for _ in range(tcn):
        n = int(input())
        divisor_chain(n)


if __name__ == '__main__':
    main()
