# _*_ coding: utf-8 _*_
# @Time : 2022/3/20 上午10:27 
# @Author : wangyefei
# @File : week-285-20220320.py
import copy
from typing import List
import collections


class Solution:
    def countHillValley2(self, nums: List[int]) -> int:
        n = len(nums)
        flag_incre = True
        flag_decre = True
        for i in range(1, n):
            if nums[i] >= nums[i - 1]:
                continue
            else:
                flag_incre = False
                break
        if flag_incre:
            return 0
        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                continue
            else:
                flag_decre = False
                break
        if flag_decre:
            return 0

        ret = 0
        for i in range(1, n - 1):
            if nums[i] != nums[i - 1]:
                ret += 1
        return ret

    def countHillValley(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        i, j, k = 0, 1, 2
        ret = 0
        while k < n:
            if nums[i] < nums[j] > nums[k]:
                ret += 1
                j = k + 1
                i = j - 1
                k = j + 1
            elif nums[j] == nums[k]:
                k += 1
            else:
                j = k
                i = j - 1
                k = j + 1
        i, j, k = 0, 1, 2
        while k < n:
            if nums[i] > nums[j] < nums[k]:
                ret += 1
                j = k + 1
                i = j - 1
                k = j + 1
            elif nums[j] == nums[k]:
                k += 1
            else:
                j = k
                i = j - 1
                k = j + 1
        return ret

    def countCollisions(self, directions: str) -> int:
        n = len(directions)
        cnt_l = 0
        cnt_r = 0
        cnt = 0
        for i in range(n):
            if directions[i] == 'R':
                cnt_r += 1
            elif directions[i] == 'S':
                cnt += cnt_r
                cnt_r = 0
            else:
                cnt += cnt_r
                cnt_r = 0
        for i in range(n - 1, -1, -1):
            if directions[i] == 'L':
                cnt_l += 1
            elif directions[i] == 'S':
                cnt += cnt_l
                cnt_l = 0
            else:
                cnt += cnt_l
                cnt_l = 0
        return cnt

    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        ret = 0
        rets = [i for i in aliceArrows]
        # print(rets)
        for state in range(4096):
            need_arrows = 0
            score = 0
            tmp = [0] * 12
            for i in range(12):
                if state & (1 << i):
                    need_arrows = need_arrows + aliceArrows[i] + 1
                    score += i
                    tmp[i] = aliceArrows[i] + 1
                else:
                    tmp[i] = 0
            if need_arrows <= numArrows:
                if ret <= score:
                    rets = [i for i in tmp]
                    rets[0] = numArrows-sum(rets[1:])
                    ret = score

        return rets


if __name__ == '__main__':
    sol = Solution()
    # numArrows = 9
    # aliceArrows = [1, 1, 0, 1, 0, 0, 2, 1, 0, 1, 2, 0]
    # numArrows = 3
    # aliceArrows = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2]
    numArrows = 89
    aliceArrows = [3, 2, 28, 1, 7, 1, 16, 7, 3, 13, 3, 5]
    ret = sol.maximumBobPoints(numArrows, aliceArrows)
    print(ret)

    # directions = "RLRSLL"
    # directions = "SSR"
    # ret = sol.countCollisions(directions)
    # print(ret)
    # nums = [8, 2, 5, 7, 7, 2, 10, 3, 6, 2]  # 6
    # nums = [57,57,57,57,57,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,85,85,85,86,86,86]
    # nums = [2,4,1,1,6,5]
    # ret = sol.countHillValley(nums)
    # print(ret)
