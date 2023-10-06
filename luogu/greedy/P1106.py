# -*- coding : utf-8 -*-
# @Time: 2023/10/5 2:36
# @Author: yefei.wang
# @File: P1106.py
import sys

sys.stdin = open('./../input.txt', 'r')

input = lambda: sys.stdin.readline().rstrip('\r\n')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

s = input()
k = I()
ss = list(s)
n = len(ss)

stk = []
for i in range(n):
    while stk and stk[-1] > ss[i] and k > 0:
        stk.pop()
        k -= 1
    stk.append(ss[i])

while k > 0:
    stk.pop()
    k -= 1

while len(stk) > 1 and stk[0] == '0':
    stk.pop(0)

print(''.join(stk))
