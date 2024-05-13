# -*- coding: utf-8 -*-
# @Time: 2024/5/13 16:11
# @Author: yfwang
# @File: 606.py
from typing import Optional

from leetcode.tree.tree_utils import TreeNode, stringToTreeNode


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        ans = []

        def dfs(node):
            ans.append(str(node.val))
            if node.left and node.right:
                ans.append('(')
                dfs(node.left)
                ans.append(')')
                ans.append('(')
                dfs(node.right)
                ans.append(')')
            elif node.left:
                ans.append('(')
                dfs(node.left)
                ans.append(')')
            elif node.right:
                ans.append('()')
                ans.append('(')
                dfs(node.right)
                ans.append(')')
        dfs(root)
        rets = ''.join(ans)
        # print(rets.count('('))
        # print(rets.count(')'))
        return rets


if __name__ == '__main__':
    s = '[1,2,3,null,4]'
    root = stringToTreeNode(s)
    ret = Solution().tree2str(root)
    print(ret)
