# _*_ coding: utf-8 _*_
# @Time : 2022/05/21 2:43 PM 
# @Author : yefe
# @File : 1110_del_nodes
from typing import List

from leetcode.tree.tree_utils import TreeNode, stringToTreeNode, treeNodeToString


class Solution:
    def delNodes(self, root, to_delete):
        to_delete_set = set(to_delete)
        res = []

        def helper(root, is_root):
            if not root: return None
            root_deleted = root.val in to_delete_set
            if is_root and not root_deleted:
                res.append(root)
            root.left = helper(root.left, root_deleted)
            root.right = helper(root.right, root_deleted)
            return None if root_deleted else root

        helper(root, True)
        return res


if __name__ == '__main__':
    input = "[1,2,3,4,5,6,7]"
    to_delete = [3, 5]
    root = stringToTreeNode(input)
    rets = Solution().delNodes(root, to_delete)
    for ret in rets:
        print(treeNodeToString(ret))

