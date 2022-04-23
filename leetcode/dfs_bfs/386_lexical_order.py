# _*_ coding: utf-8 _*_
# @Time : 2022/4/18 下午8:00 
# @Author : wangyefei
# @File : 386_lexical_order.py
from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = [0] * n
        num = 1
        for i in range(n):
            ans[i] = num
            if num * 10 <= n:
                num *= 10
            else:
                while num % 10 == 9 or num + 1 > n:
                    num //= 10
                num += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    n = 99
    ret = sol.lexicalOrder(n)
    print(ret)
