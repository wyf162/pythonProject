# -*- coding : utf-8 -*-
# @Time: 2024/3/27 23:33
# @Author: yefei.wang
# @File: D.py


import sys

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
    n, k = MI()
    nums = LI()


    def check(h):
        arr = []
        cnt = 0
        tot = 0
        for i in range(n):
            if nums[i] >= h:
                tot += 1
                x = nums[i]
                while x % k == 0 and x // k >= h:
                    x = x // k
                    cnt += 1
            else:
                x = nums[i]
                while x % k == 0:
                    x = x // k
                    cnt += 1
                if x == nums[i]:
                    arr.append(x)
        arr.sort()
        while cnt and arr:
            x = arr.pop()
            if x * k >= h and cnt:
                cnt -= 1
                tot += 1
        return h <= tot


    L, R = 0, n + 1
    ans = 0
    while L <= R:
        mid = (L + R) // 2
        # print(mid)
        if check(mid):
            ans = mid
            L = mid + 1
        else:
            R = mid - 1
    print(ans)
