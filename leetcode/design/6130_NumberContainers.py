# -*- coding : utf-8 -*-
# @Time: 2022/7/24 9:46
# @Author: yefei.wang
# @File: 6130_NumberContainers.py

from sortedcontainers import SortedSet
from collections import defaultdict

class NumberContainers2:

    def __init__(self):
        self.hst1 = dict()
        self.hst2 = dict()

    def change(self, index: int, number: int) -> None:
        if index not in self.hst1:
            self.hst1[index] = number
            if number not in self.hst2:
                self.hst2[number] = set()
            self.hst2[number].add(index)


        else:
            pre_number = self.hst1[index]
            self.hst2[pre_number].remove(index)
            self.hst1[index] = number
            if number not in self.hst2:
                self.hst2[number] = set()
            self.hst2[number].add(index)

    def find(self, number: int) -> int:
        if number not in self.hst2 or not self.hst2:
            return -1
        else:
            return min(self.hst2[number])


class NumberContainers:
    def __init__(self):
        self.m = {}
        self.ms = defaultdict(SortedSet)

    def change(self, index: int, number: int) -> None:
        if index in self.m:
            self.ms[self.m[index]].remove(index)
        self.m[index] = number
        self.ms[number].add(index)

    def find(self, number: int) -> int:
        s = self.ms[number]
        return s[0] if s else -1


if __name__ == '__main__':
    cmds = ["NumberContainers","find","change","change","change","change","find","change","find"]
    parms = [[],[10],[2,10],[1,10],[3,10],[5,10],[10],[1,20],[10]]

    number_containers = NumberContainers()
    for cmd, parm in zip(cmds[1:], parms[1:]):
        ret = getattr(number_containers, cmd)(*parm)
        print(ret)
