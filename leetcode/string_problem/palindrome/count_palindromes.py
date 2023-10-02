# _*_ coding: utf-8 _*_
# @Time : 2022/11/27 3:05 PM 
# @Author : yefe
# @File : count_palindromes

from collections import Counter
from string import digits


class Solution:
    def countPalindromes(self, s: str) -> int:
        suf = [0] * 10
        suf2 = [0] * 100
        for d in map(int, reversed(s)):
            for j, c in enumerate(suf):
                suf2[d * 10 + j] += c
            suf[d] += 1

        ans = 0
        pre = [0] * 10
        pre2 = [0] * 100
        for d in map(int, s):
            suf[d] -= 1
            for j, c in enumerate(suf):
                suf2[d * 10 + j] -= c  # 撤销
            ans += sum(c1 * c2 for c1, c2 in zip(pre2, suf2))  # 枚举所有字符组合
            for j, c in enumerate(pre):
                pre2[d * 10 + j] += c
            pre[d] += 1
        return ans % (10 ** 9 + 7)


if __name__ == '__main__':
    sol = Solution()
    s = "103301"
    ret = sol.countPalindromes(s)
    print(ret)
