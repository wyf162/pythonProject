# _*_ coding: utf-8 _*_
# @Time : 2022/08/22 10:57 PM 
# @Author : yefe
# @File : 655_printTree

from typing import List, Optional
from tree_utils import TreeNode, stringToTreeNode


class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:

        height = 0

        def get_tree_height(node, h):
            nonlocal height
            height = max(height, h)
            if node and node.left:
                get_tree_height(node.left, h + 1)
            if node and node.right:
                get_tree_height(node.left, h + 1)

        get_tree_height(root, 0)
        print(height)
        m, n = height + 1, 2 ** (height + 1) - 1
        mtx = [["" for j in range(n)] for i in range(m)]

        def fill_matrix(node, i, j):
            nonlocal mtx
            mtx[i][j] = str(node.val)
            if node and node.left:
                fill_matrix(node.left, i + 1, j - 2**(height-i-1))
            if node and node.right:
                fill_matrix(node.right, i + 1, j + 2**(height-i-1))

        fill_matrix(root, 0, (n - 1) // 2)

        return mtx


if __name__ == '__main__':
    sol = Solution()
    # root = stringToTreeNode("[1,2]")
    # root = stringToTreeNode("[1, 2, 3, null, 4]")
    root = stringToTreeNode("[10,5,15,null,null,6,20]")
    ret = sol.printTree(root)
    print(ret)
