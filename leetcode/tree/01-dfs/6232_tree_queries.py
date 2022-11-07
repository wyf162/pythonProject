# _*_ coding: utf-8 _*_
# @Time : 2022/10/30 3:59 PM 
# @Author : yefe
# @File : 6232_tree_queries

from collections import defaultdict
from typing import Optional, List

from leetcode.tree.tree_utils import TreeNode


class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        height = defaultdict(int)

        def get_height(node: Optional[TreeNode]):
            if node is None:
                return 0
            height[node] = 1 + max(get_height(node.right), get_height(node.left))
            return height[node]

        get_height(root)

        res = [0]*(len(height)+1)

        def dfs(node: Optional[TreeNode], depth: int, rest_h: int) -> None:
            if node is None:
                return
            depth += 1
            res[node.val] = rest_h
            dfs(node.left, depth, max(rest_h, depth+height[node.right]))
            dfs(node.right, depth, max(rest_h, depth+height[node.left]))

        dfs(root, -1, 0)

        for i, q in enumerate(queries):
            queries[i] = res[q]
        return queries


