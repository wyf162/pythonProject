# _*_ coding: utf-8 _*_
# @Time : 2022/05/25 9:23 PM 
# @Author : yefe
# @File : 891_sumSubseqWidths
from typing import List


class Solution(object):
    def sumSubseqWidths(self, A):
        MOD = 10**9 + 7
        N = len(A)
        A.sort()

        pow2 = [1]
        for i in range(1, N):
            pow2.append(pow2[-1] * 2 % MOD)

        ans = 0
        for i, x in enumerate(A):
            ans = (ans + (pow2[i] - pow2[N-1-i]) * x) % MOD
        return ans
