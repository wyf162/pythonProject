# _*_ coding: utf-8 _*_
# @Time : 2022/05/17 8:37 PM 
# @Author : yefe
# @File : 04009
from typing import List

from tree_utils import TreeNode, stringToTreeNode


class Solution:
    def BSTSequences(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        sequences = list()

        def dfs(nodes, sequence):
            if not nodes:
                sequences.append(sequence)
            else:
                for i in range(len(nodes)):
                    if nodes[i].left and nodes[i].right:
                        dfs(nodes[:i]+nodes[i+1:]+[nodes[i].left, nodes[i].right], sequence+[nodes[i].val])
                    elif nodes[i].left:
                        dfs(nodes[:i] + nodes[i+1:] + [nodes[i].left], sequence + [nodes[i].val])
                    elif nodes[i].right:
                        dfs(nodes[:i] + nodes[i+1:] + [nodes[i].right], sequence + [nodes[i].val])
                    else:
                        dfs(nodes[:i] + nodes[i+1:], sequence + [nodes[i].val])

        dfs([root], [])
        return sequences


if __name__ == '__main__':
    input = "[2,1,3]"
    input = "[4, 1, null, null, 3, 2]"
    input = "[]"
    root = stringToTreeNode(input)
    sol = Solution()
    ret = sol.BSTSequences(root)
    print(ret)