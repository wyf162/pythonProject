# _*_ coding: utf-8 _*_
# @Time : 2022/08/14 10:31 PM 
# @Author : yefe
# @File : 658_minCameraCover
from typing import Optional, List


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


class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> List[int]:
            if not node:
                return [1000, 0, 0]
            la, lb, lc = dfs(node.left)
            ra, rb, rc = dfs(node.right)
            a = lc + rc + 1
            b = min(a, la + rb, ra + lb)
            c = min(a, lb + rb)
            return [a, b, c]

        _, b, _ = dfs(root)
        return b

    def minCameraCover2(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> List[int]:
            if not node:
                return [1000, 0, 0]
            la, lb, lc = dfs(node.left)
            ra, rb, rc = dfs(node.right)
            a = lc + rc + 1
            b = min(a, la + rb, ra + lb)
            c = min(a, lb + rb)
            return [a, b, c]

        _, b, _ = dfs(root)
        return b


if __name__ == '__main__':
    sol = Solution()
    input = "[0, 0, null, 0, 0]"
    root = stringToTreeNode(input)
    ret = sol.minCameraCover(root)
    print(ret)
