# _*_ coding: utf-8 _*_
# @Time : 2022/08/20 1:04 PM 
# @Author : yefe
# @File : 1282_group_the_people
from collections import defaultdict
from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        hst = defaultdict(list)

        for idx, group in enumerate(groupSizes):
            hst[group].append(idx)

        rets = []
        for k, peoples in hst.items():
            for i in range(0, len(peoples), k):
                rets.append(peoples[i: i+k])
        return rets