# _*_ coding: utf-8 _*_
# @Time : 2022/05/08 10:45 AM 
# @Author : yefe
# @File : 6057_average_of_subtree
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        hst_cnt = dict()
        hst_val = dict()
        hst = dict()

        def dfs_cnt(root):
            if root.left and root.right:
                cnt = dfs_cnt(root.left) + dfs_cnt(root.right) + 1
                hst_cnt[root] = cnt
                return cnt
            elif root.left:
                cnt = dfs_cnt(root.left) + 1
                hst_cnt[root] = cnt
                return cnt
            elif root.right:
                cnt = dfs_cnt(root.right) + 1
                hst_cnt[root] = cnt
                return cnt
            else:
                hst_cnt[root] = 1
                return 1

        def dfs_val(root):
            if root.left and root.right:
                val = dfs_val(root.left) + dfs_val(root.right)+ root.val
                hst_val[root] = val
                return val
            elif root.left:
                val = dfs_val(root.left) + root.val
                hst_val[root] = val
                return val
            elif root.right:
                val = dfs_val(root.right) + root.val
                hst_val[root] = val
                return val
            else:
                hst_val[root] = root.val
                return root.val

        def dfs(root):
            if root:
                hst[root] = root.val
                dfs(root.left)
                dfs(root.right)

        dfs_cnt(root)
        dfs_val(root)
        dfs(root)

        ret = 0
        for k, v in hst.items():
            s = hst_val[k]
            c = hst_cnt[k]
            print(k.val, v, s, c)
            if s // c == v:
                ret += 1
        return ret

        # for k, v in hst_cnt.items():
        #     print(k.val, end=": ")
        #     print(v)
        #
        # for k, v in hst_val.items():
        #     print(k.val, end=": ")
        #     print(v)
        # print(hst_cnt)


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


if __name__ == '__main__':
    # line = '[4,8,5,0,1,null,6]'
    line = '[1]'
    root = stringToTreeNode(line)

    ret = Solution().averageOfSubtree(root)

    print(ret)
