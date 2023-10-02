# -*- coding : utf-8 -*-
# @Time: 2022/1/3 19:15
# @Author: yefei.wang
# @File: 01_stake_and_queue.py

from sortedcontainers import SortedList


class CQueue:

    def __init__(self):
        self.stk1 = list()
        self.stk2 = list()

    def appendTail(self, value: int) -> None:
        self.stk1.append(value)

    def deleteHead(self) -> int:
        if not self.stk2:
            while self.stk1:
                self.stk2.append(self.stk1.pop())
        if self.stk2:
            return self.stk2.pop()
        else:
            return -1


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk = list()
        self.sorted_list = SortedList()

    def push(self, x: int) -> None:
        self.stk.append(x)
        self.sorted_list.add(x)

    def pop(self) -> None:
        x = self.stk.pop()
        self.sorted_list.remove(x)

    def top(self) -> int:
        return self.stk[-1]

    def min(self) -> int:
        return self.sorted_list[0]


if __name__ == '__main__':
    cq = CQueue()
    cq.appendTail(3)
    print(cq.stk2)
    print(cq.stk1)
    data = cq.deleteHead()
    print(data)
