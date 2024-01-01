# -*- coding : utf-8 -*-
# @Time: 2023/12/17 10:37
# @Author: yefei.wang
# @File: C.py

from typing import List


def nearestPalindromic(n: str):
    if len(n) <= 1:
        return [n]
    ans = list()
    nums = list(n)
    l = len(nums)
    if l & 1:
        m = l >> 1
        x = int("".join(nums[:m + 1]))
        for d_x in [-1, 0, 1]:
            left_x = x + d_x
            left_x = list(str(left_x))
            if len(left_x) == m + 2:
                left_x = "1" + "0" * (l - 1) + "1"
            elif len(left_x) == m:
                left_x = "9" * (l - 1)
            else:
                left_x = left_x + list(reversed(left_x[:-1]))
            ans.append(int("".join(left_x)))
    else:
        m = l >> 1
        x = int("".join(nums[:m]))
        for d_x in [-1, 0, 1]:
            left_x = x + d_x
            left_x = list(str(left_x))
            if len(left_x) == m - 1 or left_x == ['0']:
                left_x = "9" * (l - 1)
            elif len(left_x) == m + 1:
                left_x = "1" + "0" * (l - 1) + "1"
            else:
                left_x = left_x + list(reversed(left_x[:]))
            ans.append(int("".join(left_x)))
    return ans


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if n % 2 == 1:
            k = nums[n >> 1]
        else:
            k = (nums[n >> 1] + nums[(n >> 1) - 1]) // 2

        cands = nearestPalindromic(str(k))
        cands = [int(x) for x in cands]
        cost, rst = None, None
        for cand in cands:
            if cost is None:
                cost = sum(abs(x - cand) for x in nums)
                rst = cand
            else:
                cost2 = sum(abs(x - cand) for x in nums)
                if cost2 < cost:
                    cost = cost2
                    rst = cand
        return cost


if __name__ == '__main__':
    sol = Solution()
    # nums = [10, 12, 13, 14, 15]
    nums = [22, 33]
    ret = sol.minimumCost(nums)
    print(ret)
