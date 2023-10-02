# _*_ coding: utf-8 _*_
# @Time : 2022/08/29 10:18 PM 
# @Author : yefe
# @File : 1363_largestMultipleOfThree

from typing import List


class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        digits.sort()
        n = len(digits)

        f = [[float("-inf")] * 3 for _ in range(n + 1)]

        f[0][0] = 0

        for i in range(1, n + 1):
            for j in range(3):
                f[i][j] = max(f[i - 1][j], f[i - 1][(j + 3 - digits[i - 1] % 3) % 3] + 1)

        if f[n][0] <= 0:
            return ""

        res = ""
        j = 0
        for i in range(n, -1, -1):
            if f[i][j] == f[i - 1][(j + 3 - digits[i - 1] % 3) % 3] + 1:
                res += str(digits[i - 1])
                j = (j + 3 - digits[i - 1] % 3) % 3
                if res == "0":
                    return res
        return res


if __name__ == '__main__':
    sol = Solution()
    digits = [8, 9, 1, 0, 0]
    ret = sol.largestMultipleOfThree(digits)
    print(ret)
