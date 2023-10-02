# _*_ coding: utf-8 _*_
# @Time : 2022/06/03 11:23 PM 
# @Author : yefe
# @File : 538_convert_bst
from typing import Optional

from leetcode.tree.tree_utils import TreeNode, string_to_treenode, treenode_to_string


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        pre = 0

        def dfs(root):
            if root:
                nonlocal pre
                dfs(root.right)
                pre += root.val
                root.val = pre
                dfs(root.left)
            else:
                return 0

        dfs(root)
        return root


if __name__ == '__main__':
    sol = Solution()
    root = string_to_treenode("[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]")
    ret = sol.convertBST(root)
    print(treenode_to_string(ret))
