# -*- coding : utf-8 -*-
# @Time: 2023/8/27 11:18
# @Author: yefei.wang
# @File: getMaxFunctionValue.py
from typing import List


class Solution:
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:
        n = len(receiver)
        circles = [[] for _ in range(n)]
        for i in range(n):
            circles[i].append(i)
            st = i
            while True:
                nex = receiver[st]
                if nex == circles[i][0]:
                    break
                else:
                    circles[i].append(nex)
                    st = nex
        ans = 0
        for i in range(n):
            tmp = sum(circles[i]) * (k // len(circles[i])) + sum(circles[i][:k % n])
            ans = max(ans, tmp)
        return ans


if __name__ == '__main__':
    sol = Solution()
    receiver = [1, 1, 1, 2, 3]
    k = 3
    ret = sol.getMaxFunctionValue(receiver, k)
    print(ret)
