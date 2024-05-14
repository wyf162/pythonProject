# -*- coding : utf-8 -*-
# @Time: 2023/11/4 8:38
# @Author: yefei.wang
# @File: 421.py
from typing import List


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.end = False


class Trie:
    def __init__(self):
        self.root = Node(-1)

    def insert(self, num):
        s = bin(num)[2:].zfill(31)
        node = self.root

        for b in s:
            if b == '0':
                if node.left is None:
                    node.left = Node(b)
                    node = node.left
                else:
                    node = node.left
            else:
                if node.right is None:
                    node.right = Node(b)
                    node = node.right
                else:
                    node = node.right
        node.end = True

    def get_xor_max(self, num):
        s = bin(num)[2:].zfill(31)
        node = self.root

        mx = 0
        k = 31
        for b in s:
            k -= 1
            if b == '0':
                if node.right is None:
                    node = node.left
                else:
                    mx |= (1 << k)
                    node = node.right
            else:
                if node.left is None:
                    node = node.right
                else:
                    mx |= (1 << k)
                    node = node.left

        return mx


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        trie .insert(nums[0])
        n = len(nums)
        rst = 0
        for i in range(1, n):
            tmp = trie.get_xor_max(nums[i])
            rst = max(rst, tmp)
            trie.insert(nums[i])
        return rst


if __name__ == '__main__':
    sol= Solution()
    nums = [3, 10, 5, 25, 2, 8]
    ret = sol.findMaximumXOR(nums)
    print(ret)































