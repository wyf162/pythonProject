# -*- coding : utf-8 -*-
# @Time: 2021/12/12 10:29
# @Author: yefei.wang
# @File: 20211212.py
import collections
from typing import List


class Solution:

    def countPoints(self, rings: str) -> int:
        ans = 0
        hst = collections.defaultdict(set)
        for i in range(0,len(rings),2):
            hst[rings[i+1]].add(rings[i])
        for k in hst.keys():
            if len(hst.get(k))>=3:
                ans += 1
        print(hst)
        return ans

    def subArrayRanges(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        if n==1:
            return ans
        for i in range(0,n-1):
            s,t = min(nums[i:i+2]), max(nums[i:i+2])
            ans += t-s
            print('t-s',t-s)
            for j in range(i+2,n):
                s = min(s,nums[j])
                t = max(t,nums[j])
                ans += t-s
                print('t-s',t-s)

        return ans

    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        ans = 0
        n = len(plants)
        i,j = 0, n-1
        ca,cb = capacityA, capacityB
        while i<j:
            if ca>=plants[i]:
                ca -= plants[i]
            else:
                ca = capacityA-plants[i]
                ans += 1
            i += 1

            if cb>=plants[j]:
                cb -= plants[j]
            else:
                cb = capacityB-plants[j]
                ans += 1
            j -= 1
        if i==j:
            if max(ca,cb)<plants[i]:
                ans += 1
        return ans

    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        hst = collections.defaultdict(int)
        for fruit in fruits:
            position, amount = fruit
            hst[position] = amount
        # left 记录往左边走i步可以获得的草莓数量
        left = [0]*(k+1)
        left[0] = hst.get(startPos,0)
        for i in range(1,k+1):
            left[i] = left[i-1]+hst.get(startPos-i,0)
        print(left)

        # right
        right = [0]*(k+1)
        right[0] = hst.get(startPos,0)
        for i in range(1,k+1):
            right[i] = right[i-1]+hst.get(startPos+i,0)

        print(right)
        ans = 0
        for i in range(k+1):
            if k-2*i>=0:
                ans= max(left[i]+right[k-2*i], ans)

        for j in range(k):
            if k-2*j>=0:
                ans= max(left[k-2*j]+right[j], ans)
        return ans-left[0]


if __name__ == "__main__":
    sol = Solution()
    fruits = [[0, 9], [4, 9], [5, 7], [6, 2], [7, 4], [10, 9]]
    # fruits = [[2, 8], [6, 3], [8, 6]]
    startPos = 5
    k = 2
    print(sol.maxTotalFruits(fruits,startPos,k))



    # plants = [2, 2, 5, 2, 2]
    # capacityA = 3
    # capacityB = 5
    # print(sol.minimumRefill(plants,capacityA,capacityB))

    # nums = [1, 2, 3]
    # nums = [4, -2, -3, 4, 1]
    # print('ans:',sol.subArrayRanges(nums))
    #
    # for j in range(4,3):
    #     print('error')
    # rings = "B0R0G0R9R0B0G0"
    # rings = "G4"
    # print(sol.countPoints(rings))