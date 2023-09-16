# -*- coding : utf-8 -*-
# @Time: 2023/9/13 20:59
# @Author: yefei.wang
# @File: 421_maxXor.py
from typing import List


class TrieNode:
    def __init__(self):
        self.children = [None] * 2


class Trie:

    def __init__(self, h):
        self.h = h
        self.root = TrieNode()

    def insert(self, num):
        node = self.root
        for i in range(self.h - 1, -1, -1):
            lr = (num >> i) & 1
            if node.children[lr] is None:
                node.children[lr] = TrieNode()
            node = node.children[lr]

    def maximum_xor(self, num):
        mx = 0

        node = self.root
        for i in range(self.h - 1, -1, -1):
            lr = (num >> i) & 1
            if node.children[lr ^ 1]:
                node = node.children[lr ^ 1]
                mx |= (1 << i)
            elif node.children[lr]:
                node = node.children[lr]
            else:
                break
        return mx


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie(30)
        trie.insert(nums[0])
        ans = 0
        for num in nums[1:]:
            mx = trie.maximum_xor(num)
            if mx > ans:
                ans = mx
            trie.insert(num)
        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [3, 10, 5, 25, 2, 8]
    ret = sol.findMaximumXOR(nums)
    print(ret)
