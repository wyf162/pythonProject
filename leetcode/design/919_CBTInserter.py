# -*- coding : utf-8 -*-
# @Time: 2022/7/25 22:59
# @Author: yefei.wang
# @File: 919_CBTInserter.py
from collections import deque


# _*_ coding: utf-8 _*_
# @Time : 2022/05/17 9:59 PM
# @Author : yefe
# @File : tree_utils.py

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
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


treenode_to_string = treeNodeToString
string_to_treenode = stringToTreeNode


class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.nodes = deque()
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if not node.left or not node.right:
                self.nodes.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def insert(self, val: int) -> int:
        node = self.nodes[0]
        new_node = TreeNode(val)

        if not node.left:
            self.nodes[0].left = new_node
        elif not node.right:
            self.nodes[0].right = new_node
            self.nodes.popleft()
        self.nodes.append(new_node)

    def get_root(self) -> TreeNode:
        return self.root


if __name__ == '__main__':
    root = stringToTreeNode("[1, 2]")
    cbt = CBTInserter(root)
    cbt.insert(3)
    cbt.insert(4)
    new_root = cbt.get_root()
    output = treeNodeToString(new_root)
    print(output)
