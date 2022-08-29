# _*_ coding: utf-8 _*_
# @Time : 2022/08/27 12:17 PM 
# @Author : yefe
# @File : 662_width_of_binary_tree

from typing import Optional
from tree_utils import TreeNode, stringToTreeNode


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        levelMin = {}

        def dfs(node: Optional[TreeNode], depth: int, index: int) -> int:
            if node is None:
                return 0
            if depth not in levelMin:
                levelMin[depth] = index  # 每一层最先访问到的节点会是最左边的节点，即每一层编号的最小值
            return max(index - levelMin[depth] + 1,
                       dfs(node.left, depth + 1, index * 2),
                       dfs(node.right, depth + 1, index * 2 + 1))

        return dfs(root, 1, 1)


if __name__ == '__main__':
    sol = Solution()
    root = stringToTreeNode("[1,3,2,5,3,null,9]")
    ret = sol.widthOfBinaryTree(root)
    print(ret)