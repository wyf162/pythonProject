# _*_ coding: utf-8 _*_
# @Time : 2022/08/14 11:11 PM 
# @Author : yefe
# @File : 987_verticalTraversal

from typing import List

from tree_utils import TreeNode


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:

        hst = []

        def dfs(node, row, col):
            if not node:
                return
            hst.append((col, row, node.val))
            dfs(node.left, row+1, col-1)
            dfs(node.right, row+1, col+1)

        dfs(root, 0 ,0)

        ans = []
        hst.sort()
        for col, row, val in hst:
            if not ans:
                ans.append([val])
                pre = col
            else:
                if pre==col:
                    ans[-1].append(val)
                else:
                    ans.append([val])
                    pre = col

        return ans


