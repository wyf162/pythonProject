# _*_ coding: utf-8 _*_
# @Time : 2022/11/20 2:00 PM 
# @Author : yefe
# @File : 6242_closest_nodes

from math import inf
from typing import List, Optional, Any

from leetcode.tree.tree_utils import TreeNode, string_to_treenode


class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        ans = []
        for query in queries:
            left = self.dfs_min(root, query)
            right = self.dfs_max(root, query)
            ans.append([left, right if right != inf else -1])
        return ans

    def dfs_min(self, root: Optional[TreeNode], val: int) -> int:
        if root is None:
            return -1
        if root.val == val:
            return root.val
        elif root.val > val:
            return self.dfs_min(root.left, val)
        elif root.val < val:
            return max(root.val, self.dfs_min(root.right, val))

    def dfs_max(self, root: Optional[TreeNode], val: int) -> float | int:
        if root is None:
            return inf
        if root.val == val:
            return root.val
        elif root.val < val:
            return self.dfs_max(root.right, val)
        elif root.val > val:
            return min(root.val, self.dfs_max(root.left, val))


if __name__ == '__main__':
    sol = Solution()
    root = string_to_treenode("[6,2,13,1,4,9,15,null,null,null,null,null,null,14]")
    queries = [2, 5, 16]
    ret = sol.closestNodes(root, queries)
    print(ret)
