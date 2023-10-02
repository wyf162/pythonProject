# -*- coding : utf-8 -*-
# @Time: 2023/9/30 19:16
# @Author: yefei.wang
# @File: 881_numRescueBoats.py

from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()
        left, right = 0, n-1
        ans = 0
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
            else:
                right -= 1
            ans += 1
        return ans
