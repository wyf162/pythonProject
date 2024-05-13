# -*- coding: utf-8 -*-
# @Time: 2024/5/13 16:33
# @Author: yfwang
# @File: 1938.py

from collections import defaultdict
from typing import List


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.end = False
        self.left_num = 0
        self.right_num = 0


class Trie:
    def __init__(self):
        self.root = Node(-1)

    def insert(self, num):
        s = bin(num)[2:].zfill(20)
        node = self.root

        for b in s:
            if b == '0':
                if node.left is None:
                    node.left = Node(b)
                    node.left_num += 1
                    node = node.left
                else:
                    node.left_num += 1
                    node = node.left
            else:
                if node.right is None:
                    node.right = Node(b)
                    node.right_num += 1
                    node = node.right
                else:
                    node.right_num += 1
                    node = node.right
        node.end = True

    def get_xor_max(self, num):
        s = bin(num)[2:].zfill(20)
        node = self.root

        mx = 0
        k = 20
        for b in s:
            k -= 1
            if b == '0':
                if node.right_num == 0 or node.right is None:
                    node = node.left
                else:
                    mx |= (1 << k)
                    node = node.right
            else:
                if node.left_num == 0 or node.left is None:
                    node = node.right
                else:
                    mx |= (1 << k)
                    node = node.left

        return mx

    def delete(self, num):
        s = bin(num)[2:].zfill(20)
        node = self.root

        for b in s:
            if b == '0':
                node.left_num -= 1
                node = node.left
            else:
                node.right_num -= 1
                node = node.right


class Solution:
    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        n = len(parents)
        tree = [[] for _ in range(n)]
        for i, p in enumerate(parents):
            if p == -1:
                root = i
            else:
                tree[p].append(i)
        # print(tree)
        m = len(queries)
        ans = [0] * m
        g = defaultdict(list)
        for i in range(m):
            x, v = queries[i]
            g[x].append((v, i))

        trie = Trie()
        stk = [(root, 0)]
        while stk:
            x, s = stk.pop()
            if s == 0:
                trie.insert(x)
                for v, i in g[x]:
                    ans[i] = trie.get_xor_max(v)
                stk.append((x, 1))
                for y in tree[x]:
                    stk.append((y, 0))
            else:
                trie.delete(x)
        return ans


if __name__ == '__main__':
    sol = Solution()
    # parents = [-1, 0, 1, 1]
    # queries = [[0, 2], [3, 2], [2, 5]]
    parents = [3, 7, -1, 2, 0, 7, 0, 2]
    queries = [[4, 6], [1, 15], [0, 5]]
    ret = sol.maxGeneticDifference(parents, queries)
    print(ret)
