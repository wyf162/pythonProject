# -*- coding : utf-8 -*-
# @Time: 2022/6/19 9:53
# @Author: yefei.wang
# @File: 508_find_frequent_tree_sum.py

from .tree_utils import TreeNode, string_to_treenode
from typing import List
from collections import defaultdict


class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:

        hst = defaultdict(int)

        def dfs(node):
            nonlocal hst
            if node.left is None and node.right is None:
                hst[node.val] += 1
                return node.val
            elif node.left is None:
                key = node.val + dfs(node.right)
                hst[key] += 1
                return key
            elif node.right is None:
                key = node.val + dfs(node.left)
                hst[key] += 1
                return key

            else:
                key = node.val + dfs(node.left) + dfs(node.right)
                hst[key] += 1
                return key

        dfs(root)
        rets = []
        target = max(hst.values())
        for k,v in hst.items():
            if v==target:
                rets.append(k)
        return rets