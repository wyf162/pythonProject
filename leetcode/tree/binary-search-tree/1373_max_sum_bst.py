# _*_ coding: utf-8 _*_
# @Time : 2022/06/04 12:27 AM 
# @Author : yefe
# @File : 1373_max_sum_bst
from typing import Optional

from leetcode.tree.tree_utils import TreeNode, string_to_treenode, treenode_to_string


class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.is_bst(root)
        self.sum_bst(root)

        ans = 0
        def preOrder(root):
            nonlocal ans
            if root:
                if root.is_bst:
                    ans = max(ans, root.sum)
                preOrder(root.left)
                preOrder(root.right)

        preOrder(root)
        return ans

    def is_bst(self, root: Optional[TreeNode]) -> bool:
        if root.left and root.right:
            left_flag = self.is_bst(root.left)
            right_flag = self.is_bst(root.right)
            # print(self.max_bst(root.left))
            # print(self.min_bst(root.right))
            root.is_bst = self.max_bst(root.left) < root.val < self.min_bst(root.right) and left_flag and right_flag
            return root.is_bst
        elif root.left:
            left_flag = self.is_bst(root.left)
            root.is_bst = self.max_bst(root.left) < root.val and left_flag
            return root.is_bst
        elif root.right:
            right_flag = self.is_bst(root.right)
            root.is_bst = self.min_bst(root.right) > root.val and right_flag
            return root.is_bst
        else:
            root.is_bst = True
            return root.is_bst

    def sum_bst(self, root: Optional[TreeNode]) -> int:
        if root.left and root.right:
            root.sum = root.val + self.sum_bst(root.left) + self.sum_bst(root.right)
            return root.sum
        elif root.left:
            root.sum = root.val + self.sum_bst(root.left)
            return root.sum
        elif root.right:
            root.sum = root.val + self.sum_bst(root.right)
            return root.sum
        else:
            root.sum = root.val
            return root.val

    def min_bst(self, root):
        if root.left:
            return self.min_bst(root.left)
        else:
            return root.val

    def max_bst(self, root):
        if root.right:
            return self.max_bst(root.right)
        else:
            return root.val


if __name__ == '__main__':
    sol = Solution()
    # inputs = "[1, 4, 3, 2, 4, 2, 5, null, null, null, null, null, null, 4, 6]"
    inputs = "[1,null,10,-5,20]"
    root = string_to_treenode(inputs)
    ret = sol.maxSumBST(root)
    print(ret)