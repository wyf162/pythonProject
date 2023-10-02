# _*_ coding: utf-8 _*_
# @Time : 2022/10/18 9:08 PM 
# @Author : yefe
# @File : 1981_minimize_difference
from collections import deque
from typing import List


class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        up = 5000

        s = set()
        s.add(0)

        for row in mat:
            ns = set()
            for y in s:
                up = 5000
                for x in row:
                    if x + y <= target:
                        ns.add(x+y)
                    else:
                        up = min(up, x + y)
            s = ns

        ret = up - target
        if s:
            ret = min(ret, target - max(s))

        return ret


if __name__ == '__main__':
    sol = Solution()
    mat = [[3, 5], [5, 10]]
    target = 47
    ret = sol.minimizeTheDifference(mat, target)
    print(ret)
