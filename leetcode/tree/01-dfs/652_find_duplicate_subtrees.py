# _*_ coding: utf-8 _*_
# @Time : 2022/09/05 9:00 PM 
# @Author : yefe
# @File : 652_find_duplicate_subtrees

from typing import Optional, List

from leetcode.tree.tree_utils import TreeNode


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        def dfs(node: Optional[TreeNode]) -> str:
            if not node:
                return ""

            serial = "".join([str(node.val), "(", dfs(node.left), ")(", dfs(node.right), ")"])
            if tree := seen.get(serial, None):
                repeat.add(tree)
            else:
                seen[serial] = node
            return serial

        seen = dict()
        repeat = set()

        dfs(root)

        return list(repeat)
