# _*_ coding: utf-8 _*_
# @Time : 2022/11/17 10:47 PM 
# @Author : yefe
# @File : 236_lowest_common_ancestor

from typing import List
from leetcode.tree.tree_utils import TreeNode, string_to_treenode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.add_parent(root)

        p_ancestor = self.find_ancestor(p)
        q_ancestor = self.find_ancestor(q)

        i = 0
        while True and i<len(p_ancestor) and i<len(q_ancestor):
            if p_ancestor[i] == q_ancestor[i]:
                i += 1
            else:
                break
        return p_ancestor[i-1] if i>=1 else root

    def add_parent(self, root: 'TreeNode'):
        if root.left:
            root.left.parent = root
            self.add_parent(root.left)
        if root.right:
            root.right.parent = root
            self.add_parent(root.right)

    def find_ancestor(self, root: 'TreeNode') -> List['TreeNode']:
        if hasattr(root, 'parent'):
            return self.find_ancestor(root.parent) + [root]
        else:
            return [root]


