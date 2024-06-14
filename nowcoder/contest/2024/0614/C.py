# -*- coding : utf-8 -*-
# @Time: 2024/6/14 19:19
# @Author: yefei.wang
# @File: C.py
import bisect
import sys
from itertools import accumulate

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

n = I()
A = LI()
PA = list(accumulate(A, initial=0))

ans = 0
for i in range(n):
    pre = PA[i + 1]
    x = max(pre, (PA[-1] - pre) // 2)
    j = bisect.bisect_right(PA, pre + x)
    if j >= n:
        continue
    else:
        ans += (n - j)

print(ans)
