# -*- coding : utf-8 -*-
# @Time: 2021/12/12 15:44
# @Author: yefei.wang
# @File: 911_TopVotedCandidate.py
from typing import List


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        n = len(times)
        hst = dict()
        res = [persons[0]]
        hst[persons[0]] = 1
        cur_candidate = persons[0]
        for i in range(1,n):
            if persons[i]==cur_candidate:
                hst[persons[i]] += 1
                res.append(persons[i])
            elif hst[cur_candidate]<=hst.get(persons[i],0)+1:
                cur_candidate = persons[i]
                hst[persons[i]] = hst.get(persons[i],0)+1
                res.append(persons[i])
            else:
                hst[persons[i]] = hst.get(persons[i],0)+1
                res.append(cur_candidate)
        self.res = res
        self.times = times

    def q(self, t: int) -> int:
        iloc = bisect(self.times,t)
        # iloc = max(iloc-1, 0)
        # print('iloc', iloc, end=" ")
        return self.res[iloc]


def bisect(nums, target):
    left, right = 0, len(nums)-1
    while left<=right:
        mid = left+(right-left>>1)
        # print(left, right, mid)
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            right = mid-1
        else:
            left = mid+1
    return min(left,right)


# 输入：
# ["TopVotedCandidate", "q", "q", "q", "q", "q", "q"]
# [[[0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]], [3], [12], [25], [15], [24], [8]]
# 输出：
# [null, 0, 1, 1, 0, 0, 1]

if __name__=="__main__":
    nums = [0, 5, 10, 15, 20, 25, 30]
    # print(bisect(nums, 28))
    # targets = [-1, 0, 3, 15, 28, 35]
    # for target in targets:
    #     print(target, bisect(nums,target))
    persons=[0, 1, 1, 0, 0, 1, 0]
    times=[0, 5, 10, 15, 20, 25, 30]
    top_voted_candidate = TopVotedCandidate(persons,times)
    print(top_voted_candidate.res)

    print(top_voted_candidate.q(3))
    print(top_voted_candidate.q(12))
    print(top_voted_candidate.q(25))

    print(top_voted_candidate.q(15))
    print(top_voted_candidate.q(24))
    print(top_voted_candidate.q(8))


