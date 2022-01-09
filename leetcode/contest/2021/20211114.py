# _*_ coding: utf-8 _*_
# @Time : 2021/11/14 上午10:29 
# @Author : wangyefei
# @File : 20211114.py

class ListNode:
    def __init__(self, val=0, nex=None):
        self.val = val
        self.nex = nex


class LinkList(object):
    def __init__(self):
        self.dummy = ListNode(-1)
        self.head = None

    def generate_from_list(self, nums):
        dummy = self.dummy
        pre = dummy
        for num in nums:
            node = ListNode(num)
            pre.nex = node
            pre = node
        self.head = self.dummy.nex

    def show(self):
        cur = self.dummy
        while cur:
            if cur.nex:
                print(cur.val, end='->')
            else:
                print(cur.val)
            cur = cur.nex

    def reverse(self, n):
        cur = self.head.nex
        tail = self.head
        for _ in range(n):
            tnd = cur.nex
            cur.nex = self.dummy.nex
            self.dummy.nex = cur
            cur = tnd
        tail.nex = cur


if __name__ == "__main__":
    link_list = LinkList()
    link_list.generate_from_list(range(8))
    link_list.show()
    link_list.reverse(5)
    link_list.show()
