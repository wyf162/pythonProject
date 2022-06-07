# _*_ coding: utf-8 _*_
# @Time : 2022/06/05 1:00 AM 
# @Author : yefe
# @File : 1367_is_sub_path
import json

from leetcode.tree.tree_utils import TreeNode, string_to_treenode


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def stringToIntegerList(input):
    return json.loads(input)


def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        n = len(nums)
        self.res = False

        def dfs(node, i):
            if i == n:
                self.res = True
            if i < n and node:
                if node.val == nums[i]:
                    dfs(node.left, i + 1)
                    dfs(node.right, i + 1)
                if node.val == nums[0]:
                    dfs(node.left, 1)
                    dfs(node.right, 1)
                else:
                    dfs(node.left, 0)
                    dfs(node.right, 0)

        dfs(root, 0)
        return self.res


if __name__ == '__main__':
    sol = Solution()
    # head = "[1, 10]"
    # root = "[1, null, 1, 10, 1, 9]"
    head = "[2, 2, 1]"
    root = "[2, null, 2, null, 2, null, 1]"
    head = stringToListNode(head)
    root = string_to_treenode(root)
    ret = sol.isSubPath(head, root)
    print(ret)
