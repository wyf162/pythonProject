# _*_ coding: utf-8 _*_
# @Time : 2021/12/5 上午10:40 
# @Author : wangyefei
# @File : 20211205.py

from typing import List
from collections import defaultdict


class Solution:

    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        hst = dict()
        for d in digits:
            hst[d] = hst.get(d, 0) + 1
        nums = []
        for x in [0, 2, 4, 6, 8]:
            if hst.get(x, 0) > 0:
                hst[x] -= 1
                for y in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    if hst.get(y, 0) > 0:
                        hst[y] -= 1
                        for z in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                            if hst.get(z, 0) > 0:
                                nums.append(x+10*y+100*z)
                        hst[y] += 1
                hst[x] += 1

        return nums

    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        hst = defaultdict(int)
        hst_s = defaultdict(list)
        hst_e = defaultdict(list)
        for i in range(len(pairs)):
            x, y = pairs[i]
            hst[x] += 1
            hst[y] += 1
            hst_s[x].append(i)
            hst_e[y].append(i)
        print(hst)
        print(hst_s)
        print(hst_e)
        s_idx = 0
        for i in range(len(pairs)):
            x,y = pairs[i]
            if hst[x]%2==1:
                s_idx = i
                break
        ans = []
        while True:
            print(ans)
            ans.append(pairs[s_idx])
            if len(ans)==len(pairs):
                break
            x, y = pairs[s_idx]
            hst[x] -= 1
            hst[y] -= 1
            print(x,y)
            print(hst)
            print(hst_e)
            print(hst_s)
            s_idx=hst_s[y].pop()
            # print(s_idx)
        return ans


if __name__=="__main__":
    sol = Solution()
    # pairs = [[5, 1], [4, 5], [11, 9], [9, 4]]
    # pairs = [[1, 3], [3, 2], [2, 1]]
    # pairs = [[1, 2], [1, 3], [2, 1]]
    # pairs = [[17,18],[18,10],[10,18]]
    pairs = [[8,5],[8,7],[0,8],[0,5],[7,0],[5,0],[0,7],[8,0],[7,8]]
    print(sol.validArrangement(pairs))



    # digits = [2, 2, 8, 8, 2]
    # print(sol.findEvenNumbers(digits))