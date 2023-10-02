# _*_ coding: utf-8 _*_
# @Time : 2022/06/03 10:52 PM 
# @Author : yefe
# @File : 501_find_mode
from typing import Optional, List
from collections import Counter

from tree_utils import TreeNode, string_to_treenode, treenode_to_string


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        nums = []

        def preOrder(root):
            if root:
                nums.append(root.val)
                preOrder(root.left)
                preOrder(root.right)

        preOrder(root)
        hst = Counter(nums)
        mode_cnt = max(hst.values())
        modes = []
        for k,v in hst.items():
            if v==mode_cnt:
                modes.append(k)
        return modes


if __name__ == '__main__':
    sol = Solution()
    root = string_to_treenode("[0]")
    ret = sol.findMode(root)
    print(ret)

