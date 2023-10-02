# _*_ coding: utf-8 _*_
# @Time : 2022/10/17 10:48 PM 
# @Author : yefe
# @File : 1997_first_day_been_in_all_rooms

from typing import List


class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        M = 10**9+7

        n = len(nextVisit)

        s = [0]*n
        for i, j in enumerate(nextVisit[:-1]):
            f = (2+s[i]-s[j])%M
            s[i+1] = (s[i]+f)%M
        return s[-1]

