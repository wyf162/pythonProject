# _*_ coding: utf-8 _*_
# @Time : 2022/06/03 4:51 PM 
# @Author : yefe
# @File : 669_trim_bst

from typing import Optional

from ..tree_utils import TreeNode, stringToTreeNode, treeNodeToString


class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val < low:
            return self.trimBST(root.right, low, high)
        elif root.val > high:
            return self.trimBST(root.left, low, high)
        else:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
            return root


if __name__ == '__main__':
    sol = Solution()
    # root = stringToTreeNode("[1,0,2]")
    # low = 1
    # high = 2
    root = stringToTreeNode("[3, 0, 4, null, 2, null, null, 1]")
    low = 1
    high = 3
    ret = sol.trimBST(root, low, high)
    print(treeNodeToString(ret))
