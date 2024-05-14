# -*- coding : utf-8 -*-
# @Time: 2024/5/14 21:12
# @Author: yefei.wang
# @File: 1626D.py
# https://codeforces.com/contest/1626/problem/D

import bisect
import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
sys.stdout = open('../output.txt', 'w')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

N = 2 * 10 ** 5 + 5
arr = [0] * N
arr[0] = 1
for x in range(1, N):
    if bin(x).count('1') == 1:
        arr[x] = 0
    else:
        arr[x] = pow(2, x.bit_length()) - x


tcn = I()
for _tcn_ in range(tcn):
    n = I()
    nums = LI()
    cnt = [0] * (n + 1)
    vis = set()
    for num in nums:
        cnt[num] += 1
        vis.add(num)
    for i in range(1, n + 1):
        cnt[i] += cnt[i - 1]
    ans = 1 << 31
    for i in sorted(vis):
        c1 = cnt[i]
        ans = min(ans, arr[c1] + arr[0] + arr[cnt[-1] - cnt[i]])
        for b in range(20):
            j = bisect.bisect_right(cnt, c1 + (1 << b))
            if j - 1 == i:
                continue
            else:
                ans = min(ans, arr[c1] + arr[cnt[j - 1] - cnt[i]], arr[cnt[-1] - cnt[j - 1]])
        if ans == 0:
            break
    print(ans)
