# -*- coding : utf-8 -*-
# @Time: 2024/6/13 0:02
# @Author: yefei.wang
# @File: G.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
TI = lambda: tuple(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')

tcn = I()
for _tcn_ in range(tcn):
    n, k, mod = MI()
    A = LI()


    def f(L, R):
        # 左闭 右闭
        if L > R:
            return 0
        elif L == R:
            return A[L]

        mid = (L + R) // 2
        ret0 = f(L, mid) + f(mid + 1, R)
        ret0 %= mod
        left = [1]
        pre_sum = [0]
        for i in range(mid, mid - k + 1, -1):
            if i < L: break
            left.append(left[-1] * A[i])
            pre_sum.append(pre_sum[-1] + left[-1])

        right = [1]
        for i in range(mid + 1, mid + k, 1):
            if i > R: break
            right.append(right[-1] * A[i])

        ret1 = 0
        for i in range(1, len(right)):
            ret1 += right[i] * pre_sum[min(k - i, len(pre_sum) - 1)]
            ret1 %= mod
            # for j in range(1, len(left)):
            #     if i + j > k : break
            #     ret1 += right[i] * left[j]
            #     ret1 %= mod
        ret = ret0 + ret1
        ret %= mod
        return ret


    ans = f(0, n - 1)
    print(ans)
