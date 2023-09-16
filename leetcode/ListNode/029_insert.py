# -*- coding : utf-8 -*-
# @Time: 2022/6/18 0:57
# @Author: yefei.wang
# @File: 029_insert.py


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    @classmethod
    def init_from_list(cls, nums):
        begin = Node(nums[0])
        cur = begin
        for i in range(1, len(nums)):
            cur.next = Node(nums[i])
            cur = cur.next
        cur.next = begin
        return begin


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        node = Node(insertVal)
        if head is None:
            node.next = node
            return node
        elif head.next == head:
            head.next = node
            node.next = head
            return head
        else:
            cur = head
            nex = head.next
            while nex != head:
                if cur.val <= insertVal <= nex.val:
                    break
                else:
                    if cur.val > nex.val:
                        if insertVal > cur.val or insertVal < nex.val:
                            break
                    cur = cur.next
                    nex = nex.next
            cur.next = node
            node.next = nex
            return node
