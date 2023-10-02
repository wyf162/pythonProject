# _*_ coding: utf-8 _*_
# @Time : 2022/08/14 4:24 PM 
# @Author : yefe
# @File : 600_find_integers
from functools import cache


class Solution2:

    def findIntegers(self, n: int) -> int:
        s = bin(n)[2:]
        s = s[::-1]

        # print(s)

        @cache
        def dfs(pos: int, pre: int, limit: int):
            if pos == -1:
                return 1

            up = int(s[pos]) if limit else 1
            ans = 0
            for i in range(0, up + 1):
                if pre == 1 and i == 1:
                    continue
                else:
                    ans += dfs(pos - 1, i, limit and i == up)
            return ans

        return dfs(len(s) - 1, 0, 1)


class Solution:
    def findIntegers(self, n: int) -> int:
        dp = [0] * 31
        dp[0] = 1
        dp[1] = 1
        for i in range(2, 31):
            dp[i] = dp[i - 1] + dp[i - 2]

        pre = 0
        res = 0

        for i in range(29, -1, -1):
            val = (1 << i)
            if n & val:
                res += dp[i + 1]
                if pre == 1:
                    break
                pre = 1
            else:
                pre = 0

            if i == 0:
                res += 1

        return res


if __name__ == '__main__':
    sol = Solution()
    for n in [1, 2, 5]:
        ret = sol.findIntegers(n)
        print(ret)
