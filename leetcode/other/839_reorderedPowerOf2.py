# _*_ coding: utf-8 _*_
# @Time : 10/28/21 10:36 PM 
# @Author : wangyefei
# @File : 839_reorderedPowerOf2.py

from collections import Counter


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        x = 1
        ans = []
        while x<1e9:
            sd = Counter(list(str(x)))
            ans.append(sd)
            x = x*2
        if Counter(list(str(n))) in ans:
            return True
        else:
            return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.reorderedPowerOf2(46))

