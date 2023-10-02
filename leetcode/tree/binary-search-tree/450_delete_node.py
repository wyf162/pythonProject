# _*_ coding: utf-8 _*_
# @Time : 2022/06/02 10:07 PM 
# @Author : yefe
# @File : 450_delete_node
from typing import Optional

from tree_utils import TreeNode, stringToTreeNode, treeNodeToString


class Solution:
    def deleteNode2(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        cur, cur_parent = root, None
        while cur and cur.val != key:
            cur_parent = cur
            cur = cur.left if cur.val > key else cur.right

        if cur is None:
            return root
        if cur.left is None and cur.right is None:
            cur = None
        elif cur.right is None:
            cur = cur.left
        elif cur.left is None:
            cur = cur.right
        else:
            successor, successor_parent = cur.right, cur
            while successor.left:
                successor_parent = successor
                successor = successor.left
            if successor_parent.val == cur.val:
                successor_parent.right = successor.right
            else:
                successor_parent.left = successor.right
            successor.right = cur.right
            successor.left = cur.left
            cur = successor
        if cur_parent is None:
            return cur
        if cur_parent.left and cur_parent.left.val == key:
            cur_parent.left = cur
        else:
            cur_parent.right = cur
        return root

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.left is None or root.right is None:
            root = root.left if root.left else root.right
        else:
            successor = root.right
            while successor.left:
                successor = successor.left
            successor.right = self.deleteNode(root.right, successor.val)
            successor.left = root.left
            return successor
        return root


if __name__ == '__main__':
    sol = Solution()
    root = stringToTreeNode("[5, 2, 8, 1, 4, 6, 9, 0, null, 3, null, null, 7]")
    print(treeNodeToString(root))
    low = 1
    high = 3
    ret = sol.deleteNode(root, 2)
    print(treeNodeToString(ret))
