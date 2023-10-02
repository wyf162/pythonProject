# -*- coding : utf-8 -*-
# @Time: 2022/1/8 0:13
# @Author: yefei.wang
# @File: 89_gray_code.py
from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        gray_list = ['0', '1']
        i = 1
        while i<n:
            gray_list = ['0'+x for x in gray_list]+['1'+x for x in reversed(gray_list)]
            i = i+1
        return [int(x,2) for x in gray_list]


if __name__ == '__main__':
    sol = Solution()
    data = sol.grayCode(16)
    print(data)