# -*- coding : utf-8 -*-
# @Time: 2024/7/7 10:21
# @Author: yefei.wang
# @File: B.py

from typing import List


class Solution:
    def validStrings(self, n: int) -> List[str]:
        rets = []
        for i in range(1 << n):
            s = bin(i)[2:].zfill(n)
            if '00' in s:
                continue
            else:
                rets.append(s)
        return rets


if __name__ == '__main__':
    sol = Solution()
    n = 1
    ret = sol.validStrings(n)
    print(ret)
