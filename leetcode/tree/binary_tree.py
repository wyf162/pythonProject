# _*_ coding: utf-8 _*_
# @Time : 2021/12/5 下午12:50 
# @Author : wangyefei
# @File : binary_tree.py
from collections import deque
from typing import Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree(object):
    def __init__(self, root=None):
        self.root = root

    @classmethod
    def init_tree_from_list(cls, nodes):
        tree = BinaryTree(TreeNode(nodes.pop(0)))
        dq = deque()
        dq.append(tree.root)
        while nodes:
            for _ in range(len(dq)):
                node = dq.popleft()
                if nodes:
                    val = nodes.pop(0)
                    if val is not None:
                        node.left = TreeNode(val)
                        dq.append(node.left)
                if nodes:
                    val = nodes.pop(0)
                    if val is not None:
                        node.right = TreeNode(val)
                        dq.append(node.right)
        return tree

    @staticmethod
    def inOrder(node):
        if node is None:
            return []
        else:
            return BinaryTree.inOrder(node.left) + [node.val] + BinaryTree.inOrder(node.right)

    def levelOrder(self, node):
        ans = []
        dq = deque()
        dq.append(node)
        while dq:
            node = dq.popleft()
            ans.append(node.val)
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)
        return ans

    @staticmethod
    def find_node(root, val):
        if root is None:
            return root
        if root.val == val:
            return ''
        left = BinaryTree.find_node(root.left, val)
        right = BinaryTree.find_node(root.right,val)
        if left is not None:
            return 'L'+left
        if right is not None:
            return 'R'+right


class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def helper(node, tar):
            if node is None: return node
            if node.val == tar:
                return ''

            left = helper(node.left, tar)
            right = helper(node.right, tar)

            if left is not None:
                return 'L' + left
            if right is not None:
                return 'R' + right

        pathS = helper(root, startValue)
        pathD = helper(root, destValue)

        pubL = 0
        for i, j in zip(pathS, pathD):
            if i == j:
                pubL += 1
            else:
                break

        return 'U' * (len(pathS[pubL:])) + pathD[pubL:]


if __name__ == "__main__":
    nodes = [5, 1, 2, 3, None, 6, 4]
    my_tree = BinaryTree.init_tree_from_list(nodes)
    print(BinaryTree.find_node(my_tree.root,6))
    # print(my_tree.inOrder(my_tree.root))
    # print(my_tree.levelOrder(my_tree.root))
    # sol = Solution()
    # print(sol.getDirections(my_tree.root, 3, 6))
