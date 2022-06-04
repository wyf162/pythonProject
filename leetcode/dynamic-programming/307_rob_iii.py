# _*_ coding: utf-8 _*_
# @Time : 2022/05/14 8:51 PM 
# @Author : yefe
# @File : rob
# Definition for a binary tree node.
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:
        f = defaultdict(int)
        g = defaultdict(int)

        def dfs(node):
            if not node:
                return 0
            dfs(node.left)
            dfs(node.right)
            f[node] = node.val+g[node.left]+g[node.right]
            g[node] = max(f[node.left], g[node.left])+max(f[node.right], g[node.right])

        dfs(root)
        return max(f[root], g[root])

    def rob2(self, root: TreeNode) -> int:

        if root is None:
            return 0
        money = root.val
        if root.left:
            money += self.rob2(root.left.left) + self.rob2(root.left.right)
        if root.right:
            money += self.rob2(root.right.left) + self.rob2(root.right.right)
        return max(money, self.rob2(root.left)+self.rob2(root.right))


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


def main():
    # line = "[3,2,3,null,3,null,1]"
    line = "[3,4,5,1,3,null,1]"
    root = stringToTreeNode(line)

    ret = Solution().rob(root)

    out = str(ret)
    print(out)


if __name__ == '__main__':
    main()
