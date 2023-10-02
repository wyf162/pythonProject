# -*- coding : utf-8 -*-
# @Time: 2023/10/2 12:07
# @Author: yefei.wang
# @File: 1145_btreeGameWinningMove.py

from typing import Optional

from leetcode.tree.binary_tree import TreeNode


class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:

        size = [0] * (n + 1)
        left = 0
        right = 0

        def dfs(node):
            if node is None:
                return 0
            if node.val == x:
                nonlocal left, right
                left = node.left.val if node.left else 0
                right = node.right.val if node.right else 0
            size[node.val] += 1
            size[node.val] += dfs(node.left)
            size[node.val] += dfs(node.right)
            return size[node.val]

        dfs(root)

        if size[x] * 2 < n or size[left] * 2 > n or size[right] * 2 > n:
            return True
        else:
            return False
