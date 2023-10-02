# _*_ coding: utf-8 _*_
# @Time : 2022/08/14 11:27 PM 
# @Author : yefe
# @File : 1028_recoverFromPreorder


from typing import Optional, List
from collections import defaultdict

from tree_utils import stringToTreeNode, TreeNode


class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        path, pos = list(), 0
        while pos < len(traversal):
            level = 0
            while traversal[pos] == '-':
                level += 1
                pos += 1
            value = 0
            while pos < len(traversal) and traversal[pos].isdigit():
                value = value * 10 + (ord(traversal[pos]) - ord('0'))
                pos += 1
            node = TreeNode(value)
            if level == len(path):
                if path:
                    path[-1].left = node
            else:
                path = path[:level]
                path[-1].right = node
            path.append(node)
        return path[0]