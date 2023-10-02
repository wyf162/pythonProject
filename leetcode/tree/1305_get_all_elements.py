# _*_ coding: utf-8 _*_
# @Time : 2022/05/00 4:27 PM
# @Author : yefe
# @File : 1305_get_all_elements
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def string_to_treenode(input):
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


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def dfs(root):
            if not root:
                return []
            else:
                return dfs(root.left)+[root.val]+dfs(root.right)

        nums1 = dfs(root1)
        nums2 = dfs(root2)
        return sorted(nums1+nums2)


if __name__ == '__main__':
    sol = Solution()
    root1 = string_to_treenode('2,1,4')
    root2 = string_to_treenode("1,0,3")
    ret = sol.getAllElements(root1, root2)
    print(ret)
