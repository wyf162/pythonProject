# _*_ coding: utf-8 _*_
# @Time : 2022/4/15 下午10:51 
# @Author : wangyefei
# @File : 17012.py
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def convertBiNode(self, root: TreeNode) -> TreeNode:
        stk = list()
        node = root
        pre = None
        while stk or node:
            while node:
                stk.append(node)
                node = node.right

            if stk:
                node = stk.pop()
                if pre:
                    node.right = pre
                    pre = node
                else:
                    pre = node
                node = node.left
                pre.left = None
        return pre

    def convert_binode(self, root: TreeNode) -> TreeNode:
        self.pre = self.ans = None

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            root.left = None
            if self.pre:
                self.pre.right = root
            if self.pre is None:
                self.ans = root
            self.pre = root

            dfs(root.right)

        dfs(root)
        return self.ans


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


def ptree(root):
    while root:
        print(root.val, end=' ')
        root = root.right


if __name__ == '__main__':
    line = "[4,2,5,1,3,null,6,0]"
    root = stringToTreeNode(line)
    ret = Solution().convertBiNode(root)
    out = treeNodeToString(ret)
    print(out)

# def main():
#     import sys
#     import io
#     def readlines():
#         for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
#             yield line.strip('\n')
#
#     lines = readlines()
#     while True:
#         try:
#             line = next(lines)
#             root = stringToTreeNode(line)
#
#             ret = Solution().convertBiNode(root)
#
#             out = treeNodeToString(ret)
#             print(out)
#         except StopIteration:
#             break
