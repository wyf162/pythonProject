# -*- coding : utf-8 -*-
# @Time: 2024/3/6 22:48
# @Author: yefei.wang
# @File: E.py

import sys
from string import ascii_lowercase

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    s = list(input())
    n = len(s)
    ans = n
    for c in ascii_lowercase:
        cnt = s.count(c)
        if cnt == 0:
            continue
        nums = [0]
        for i in range(n):
            nums.append(nums[-1] + int(s[i] == c))
            if i+1 >= cnt:
                ans = min(ans, cnt - (nums[-1] - nums[-1 - cnt]))
    print(ans)
