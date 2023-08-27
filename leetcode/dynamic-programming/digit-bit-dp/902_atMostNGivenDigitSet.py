# _*_ coding: utf-8 _*_
# @Time : 2022/08/14 6:32 PM 
# @Author : yefe
# @File : 902_atMostNGivenDigitSet
from functools import cache
from typing import List


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        s = str(n)

        @cache
        def f(i: int, is_limit: bool, is_num: bool) -> int:
            if i == len(s):
                return int(is_num)
            res = 0
            if not is_num:  # 可以跳过当前数位
                res = f(i + 1, False, False)
            up = s[i] if is_limit else '9'
            for d in digits:  # 枚举要填入的数字 d
                if d > up: break
                res += f(i + 1, is_limit and d == up, True)
            return res

        return f(0, True, False)


if __name__ == '__main__':
    sol = Solution()
    digits = ["1", "3", "5", "7"]
    n = 100
    ret = sol.atMostNGivenDigitSet(digits, n)
    print(ret)
