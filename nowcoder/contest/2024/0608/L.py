# -*- coding : utf-8 -*-
# @Time: 2024/6/8 15:55
# @Author: yefei.wang
# @File: L.py
# manacher

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

n, m = MI()
s = input()
hst = dict()
for _ in range(m):
    c, v = input().split()
    hst[c] = int(v)

A = []
B = []
for c in s:
    if A and c == A[-1]:
        B[-1] += 1
    else:
        A.append(c)
        B.append(1)


def longest_palindrome(s):
    n_str = '#' + '#'.join(s) + '#'
    p = [0] * len(n_str)
    mx, loc = 0, 0
    index, maxlen = 0, 0
    for i in range(len(n_str)):
        if i < mx and 2 * loc - i < len(n_str):
            p[i] = min(mx - i, p[2 * loc - i])
        else:
            p[i] = 1

        while p[i] + i < len(n_str) and i - p[i] >= 0 and n_str[
            i - p[i]] == n_str[i + p[i]]:
            p[i] += 1

        if i + p[i] > mx:
            mx = i + p[i]
            loc = i

        if p[i] > maxlen:
            index = i
            maxlen = p[i]
    nums = []
    for i in range(1, len(p), 2):
        nums.append(p[i] // 2)
    return nums


D = longest_palindrome(A)
print(D)
# D = [1] * len(A)
# i = 1
# while i < len(A):
#     k = 1
#     while i - k >= 0 and i + k < len(A) and A[i - k] == A[i + k]:
#         k += 1
#     D[i] = k
#     i += 1

pre_sum = [0]
for i in range(len(A)):
    pre_sum.append(pre_sum[-1] + B[i] * hst[A[i]])

ans = 0
for i in range(len(A)):
    tmp = pre_sum[D[i] + i] - pre_sum[i + 1 - D[i]] + hst[A[i]]
    ans = max(ans, tmp)
print(ans)
