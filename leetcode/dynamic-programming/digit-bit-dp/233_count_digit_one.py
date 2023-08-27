# _*_ coding: utf-8 _*_
# @Time : 2022/08/14 3:21 PM 
# @Author : yefe
# @File : 233_count_digit_one


class Solution:
    def countDigitOne(self, n: int) -> int:
        s = str(n)

        def f(i: int, sk: int,  is_limit: bool):
            if i == len(s):
                return sk
            res = 0
            up = int(s[i]) if is_limit else 9
            for j in range(0, up + 1):
                if j == 1:
                    res += f(i + 1, sk+1, is_limit and j == up)
                else:
                    res += f(i + 1, sk, is_limit and j == up)
            return res

        return f(0, 0, True)


if __name__ == '__main__':
    sol = Solution()
    n = 0
    ret = sol.countDigitOne(n)
    print(ret)
