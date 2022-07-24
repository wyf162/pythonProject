# -*- coding : utf-8 -*-
# @Time: 2022/7/19 22:19
# @Author: yefei.wang
# @File: 731_myCalendarTwo.py


class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.val = 0
        self.add = 0


class MyCalendarTwo:

    def __init__(self):
        self.root = Node()
        self.n = 10 ** 9

    def update(self, node, start, end, l, r, val):
        if l <= start and end <= r:
            node.val += val
            node.add += val
            return
        self.push_down(node)
        mid = (start + end) >> 1
        if l <= mid:
            self.update(node.left, start, mid, l, r, val)
        if r > mid:
            self.update(node.right, mid + 1, end, l, r, val)
        self.push_up(node)

    def query(self, node, start, end, l, r):
        if l <= start and end <= r:
            return node.val
        self.push_down(node)
        mid = (start + end) >> 1
        ans = 0
        if l <= mid:
            ans = self.query(node.left, start, mid, l, r)
        if r > mid:
            ans = max(ans, self.query(node.right, mid + 1, end, l, r))
        return ans

    @staticmethod
    def push_down(node):
        if node.left is None:
            node.left = Node()
        if node.right is None:
            node.right = Node()
        if node.add == 0:
            return
        node.left.val += node.add
        node.right.val += node.add
        node.left.add += node.add
        node.right.add += node.add
        node.add = 0

    @staticmethod
    def push_up(node):
        node.val = max(node.left.val, node.right.val)

    def book(self, start: int, end: int) -> bool:
        if self.query(self.root, 0, self.n, start, end - 1) == 2:
            return False
        else:
            self.update(self.root, 0, self.n, start, end - 1, 1)
            return True


if __name__ == '__main__':
    my_calendar = MyCalendarTwo()
    ret = my_calendar.book(10, 20)
    print(ret)
    ret = my_calendar.book(15, 25)
    print(ret)
    ret = my_calendar.book(20, 30)
    print(ret)
