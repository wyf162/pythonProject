# _*_ coding: utf-8 _*_
# @Time : 2022/05/22 7:13 PM 
# @Author : yefe
# @File : 729_my_canlendat
import bisect


from sortedcontainers import SortedDict


class MyCalendar:

    def __init__(self):
        self.end_start = SortedDict()

    def book(self, start: int, end: int) -> bool:
        ID = self.end_start.bisect_right(start)
        if 0 <= ID < len(self.end_start):
            if self.end_start.values()[ID] < end:
                return False
        self.end_start[end] = start
        return True


class Node:
    __slots__ = 'start', 'end', 'left', 'right'
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = self.right = None

    def insert(self, node):
        if node.start >= self.end:
            if not self.right:
                self.right = node
                return True
            return self.right.insert(node)
        elif node.end <= self.start:
            if not self.left:
                self.left = node
                return True
            return self.left.insert(node)
        else:
            return False


class MyCalendar2(object):
    def __init__(self):
        self.root = None

    def book(self, start, end):
        if self.root is None:
            self.root = Node(start, end)
            return True
        return self.root.insert(Node(start, end))


if __name__ == '__main__':
    my_calendar = MyCalendar()
    ret = my_calendar.book(10, 20)
    print(ret)
    ret = my_calendar.book(15, 25)
    print(ret)
    ret = my_calendar.book(20, 30)
    print(ret)
