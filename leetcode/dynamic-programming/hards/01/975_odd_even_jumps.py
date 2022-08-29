# _*_ coding: utf-8 _*_
# @Time : 2022/08/28 3:12 PM 
# @Author : yefe
# @File : 975_odd_even_jumps
from collections import defaultdict, deque
from typing import List


class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        N = n = len(arr)

        # next great element
        nge = dict()

        stk = []

        for i, a in enumerate(arr):
            while stk and arr[stk[-1]] <= arr[i]:
                nge[stk[-1]] = i
                stk.pop()
            stk.append(i)
        # print(nge)

        # next less element
        nle = dict()
        stk = []

        for i, a in enumerate(arr):
            while stk and arr[stk[-1]] >= arr[i]:
                nle[stk[-1]] = i
                stk.pop()
            stk.append(i)
        # print(nle)

        odd = [False] * N
        even = [False] * N
        odd[N - 1] = even[N - 1] = True

        for i in range(N - 2, -1, -1):
            if nge.get(i) is not None:
                odd[i] = even[nge[i]]
            if nle.get(i) is not None:
                even[i] = odd[nle[i]]

        return sum(odd)


if __name__ == '__main__':
    sol = Solution()
    arr = [10, 13, 12, 14, 15]
    # arr = [2, 3, 1, 1, 4]
    # arr = [5, 1, 3, 4, 2]
    ret = sol.oddEvenJumps(arr)
    print(ret)
