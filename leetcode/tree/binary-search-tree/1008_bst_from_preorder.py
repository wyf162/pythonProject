# _*_ coding: utf-8 _*_
# @Time : 2022/06/04 12:10 AM 
# @Author : yefe
# @File : 1008_bst_from_preorder
from typing import List, Optional

from leetcode.tree.tree_utils import TreeNode, treenode_to_string


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        i = 1
        while i < len(preorder):
            if preorder[i] < preorder[0]:
                i += 1
            else:
                break
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])

        return root


if __name__ == '__main__':
    sol = Solution()
    # preorder = [8,5,1,7,10,12]
    preorder = [4, 2]
    root = sol.bstFromPreorder(preorder)
    print(treenode_to_string(root))
