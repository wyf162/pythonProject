# _*_ coding: utf-8 _*_
# @Time : 2022/08/21 11:00 PM
# @Author : yefe
# @File : 1932_canMerge

from typing import List, Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def arrayToTreeNode(nodes: List[int]):

    inputValues = nodes
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"


class Solution:
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        leaves = set()
        candidates = dict()

        for tree in trees:
            if tree.left:
                leaves.add(tree.left.val)
            if tree.right:
                leaves.add(tree.right.val)
            candidates[tree.val] = tree

        prev = float("-inf")

        def dfs(tree: Optional[TreeNode]) -> bool:
            if not tree:
                return True

            if not tree.left and not tree.right and tree.val in candidates:
                tree.left = candidates[tree.val].left
                tree.right = candidates[tree.val].right
                candidates.pop(tree.val)

            if not dfs(tree.left):
                return False

            nonlocal prev

            if tree.val<=prev:
                return False

            prev = tree.val

            return dfs(tree.right)

        for tree in trees:
            if tree.val not in leaves:
                candidates.pop(tree.val)
                return tree if dfs(tree) and not candidates else None
        return None


if __name__ == '__main__':
    sol = Solution()
    inputs = [[2,1],[3,2,5],[5,4]]
    trees = []
    for x in inputs:
        trees.append(arrayToTreeNode(x))

    ret = sol.canMerge(trees)
    print(treeNodeToString(ret))

