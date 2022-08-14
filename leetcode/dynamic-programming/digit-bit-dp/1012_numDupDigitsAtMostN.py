# _*_ coding: utf-8 _*_
# @Time : 2022/08/14 7:10 PM 
# @Author : yefe
# @File : 1012_numDupDigitsAtMostN
from functools import cache


class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        s = str(n)

        @cache
        def f(i: int, mask: int, is_limit: bool, is_num: bool, is_valid: bool) -> int:
            if i == len(s):
                return int(is_num and is_valid)
            res = 0
            if not is_num:  # 可以跳过当前数位
                res = f(i + 1, mask, False, False, is_valid)
            up = int(s[i]) if is_limit else 9
            for d in range(0 if is_num else 1, up + 1):  # 枚举要填入的数字 d
                if mask >> d & 1 == 0:  # d 不在 mask 中
                    res += f(i + 1, mask | (1 << d), is_limit and d == up, True, False or is_valid)
                else:
                    res += f(i + 1, mask | (1 << d), is_limit and d == up, True, True or is_valid)
            return res

        return f(0, 0, True, False, False)


if __name__ == '__main__':
    sol = Solution()
    n = 20
    ret = sol.numDupDigitsAtMostN(n)
    print(ret)
