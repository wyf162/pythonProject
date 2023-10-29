# -*- coding : utf-8 -*-
# @Time: 2023/10/14 15:03
# @Author: yefei.wang
# @File: c.py
import sys

sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))


def revert(n):
    a = list(range(n))
    for i in range(n):
        for j in range(i // 2 + 1):
            a[j], a[i - j] = a[i - j], a[j]
    print(a)

    idxs = [0] * n
    i, j, k = 0, n - 1, n - 1
    while i < j:
        idxs[i] = k
        k -= 1
        idxs[j] = k
        k -= 1
        i += 1
        j -= 1
    print(idxs)


def solve2(a):
    n = len(a)
    for i in range(n):
        for j in range(i // 2 + 1):
            a[j], a[i - j] = a[i - j], a[j]
        for j in range(i + 1):
            a[j] ^= 1
    print(a)


def solve(a):
    n = len(a)
    diff = [0] * (n + 1)
    for i in range(n):
        diff[0] += 1
        diff[i + 1] -= 1

    pre_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        pre_sum[i] = pre_sum[i - 1] + diff[i - 1]

    for i in range(n):
        if pre_sum[i + 1] % 2:
            a[i] ^= 1
    # print(a)

    idxs = [0] * n
    i, j, k = 0, n - 1, n - 1
    while i < j:
        idxs[i] = k
        k -= 1
        idxs[j] = k
        k -= 1
        i += 1
        j -= 1
    # print(idxs)
    ans = [0] * n
    for i in range(n):
        ans[i] = a[idxs[i]]
    print(' '.join(map(str, ans)))


n = I()
a = LI()
solve(a)

# if __name__ == '__main__':
#     n = I()
#     a = LI()
#     solve(a)
#     print(a)
#     solve2(a)
