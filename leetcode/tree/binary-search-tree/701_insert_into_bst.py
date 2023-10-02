# _*_ coding: utf-8 _*_
# @Time : 2022/06/03 11:45 PM 
# @Author : yefe
# @File : 701_insert_into_bst
from leetcode.tree.tree_utils import TreeNode


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return TreeNode(val)

        node = root
        pre = node
        
        while node:
            if val < node.val:
                pre = node
                node = node.left
            elif val > node.val:
                pre = node
                node = node.right
        if val<pre.val:
            pre.left = TreeNode(val)
        else:
            pre.right = TreeNode(val)

        return root
