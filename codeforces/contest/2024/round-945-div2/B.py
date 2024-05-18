# -*- coding : utf-8 -*-
# @Time: 2024/5/17 22:40
# @Author: yefei.wang
# @File: B.py

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

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    nums = LI()


    def get_val(bits):
        x = 0
        for b in range(20):
            if bits[b] >= 1:
                x |= 1 << b
        return x


    def check(k):
        bits = [0] * 20
        for i in range(k):
            for b in range(20):
                if nums[i] >> b & 1:
                    bits[b] += 1
        or_ = get_val(bits)

        for i in range(k, n):
            for b in range(20):
                if nums[i - k] >> b & 1:
                    bits[b] -= 1
                if nums[i] >> b & 1:
                    bits[b] += 1
            tmp = get_val(bits)
            if tmp != or_:
                return False
        return True


    L, R = 1, n
    ans = n
    while L <= R:
        mid = (L + R) // 2
        if check(mid):
            ans = mid
            R = mid - 1
        else:
            L = mid + 1
    print(ans)
