# -*- coding: utf-8 -*-
# @Time: 2024/6/4 17:45
# @Author: yfwang
# @File: 13E.py
# https://codeforces.com/problemset/problem/13/E
# blocks

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

n, q = MI()
nums = LI()

block_size = 400
block_num = (n + block_size - 1) // block_size


def update(i):
    new_i = i + nums[i]
    block_num_diff = new_i // block_size - i // block_size
    if block_num_diff or new_i >= n:
        out_to[i] = i
        steps[i] = 0
    else:
        out_to[i] = out_to[new_i]
        steps[i] = steps[new_i] + 1


out_to = [0] * n
steps = [0] * n

for i in range(n - 1, -1, -1):
    update(i)

tmp = 0
for _ in range(q):
    query = LI()
    if query[0] == 0:
        p, x = query[1] - 1, query[2]
        nums[p] = x
        block_idx = p // block_size
        for i in range(p, block_idx * block_size - 1, -1):
            update(i)
    else:
        tmp += 1
        pos = query[1] - 1
        ans = 0
        while pos < n:
            ans += steps[pos] + 1
            pos = out_to[pos]
            last_p = pos
            pos += nums[pos]
        print(last_p + 1, ans)
