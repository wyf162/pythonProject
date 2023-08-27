# _*_ coding: utf-8 _*_
# @Time : 2022/08/23 9:28 PM 
# @Author : yefe
# @File : 940_distinct_subseq
import copy


class Solution:
    def distinctSubseqII2(self, s: str) -> int:
        MOD = 10 ** 9 + 7

        f = [0] * 26

        sf = 0
        for a in s:
            i = ord(a) - ord('a')
            tmp = sf - f[i]
            f[i] = (sf + 1) % MOD
            sf = (tmp + f[i]) % MOD
        return sf % MOD

    def distinctSubseqII(self, s: str) -> int:
        MOD = 10 ** 9 + 7

        n = len(s)
        f = [[0] * 26 for _ in range(n + 1)]

        for i, a in enumerate(s):
            j = ord(a) - ord('a')
            for jj in range(26):
                if jj == j:
                    f[i + 1][j] = sum(f[i]) + 1
                else:
                    f[i + 1][j] = f[i][j]

        return sum(f[-1]) % MOD


if __name__ == '__main__':
    sol = Solution()
    s = "abc"
    ret = sol.distinctSubseqII(s)
    print(ret)
