# _*_ coding: utf-8 _*_
# @Time : 2022/11/05 8:26 PM 
# @Author : yefe
# @File : 1402_max_satisfaction

from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        pres = [0]
        for a in satisfaction:
            pres.append(pres[-1]+a)
        ret = 0
        s = 0
        for i, a in enumerate(satisfaction):
            s = s + pres[i] + a
            ret = max(ret, s)
        return ret


if __name__ == '__main__':
    sol = Solution()
    satisfaction = [-1, -8, 0, 5, -9]
    ret = sol.maxSatisfaction(satisfaction)
    print(ret)
