# -*- coding : utf-8 -*-
# @Time: 2023/11/12 10:29
# @Author: yefei.wang
# @File: week-371.py

from typing import List


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.end = False
        self.left_num = 0
        self.right_num = 0


class Trie:
    def __init__(self):
        self.root = Node(-1)

    def insert(self, num):
        s = bin(num)[2:].zfill(20)
        node = self.root

        for b in s:
            if b == '0':
                if node.left is None:
                    node.left = Node(b)
                    node.left_num += 1
                    node = node.left
                else:
                    node.left_num += 1
                    node = node.left
            else:
                if node.right is None:
                    node.right = Node(b)
                    node.right_num += 1
                    node = node.right
                else:
                    node.right_num += 1
                    node = node.right
        node.end = True

    def get_xor_max(self, num):
        s = bin(num)[2:].zfill(20)
        node = self.root

        mx = 0
        k = 20
        for b in s:
            k -= 1
            if b == '0':
                if node.right_num == 0 or node.right is None:
                    node = node.left
                else:
                    mx |= (1 << k)
                    node = node.right
            else:
                if node.left_num == 0 or node.left is None:
                    node = node.rightgi
                else:
                    mx |= (1 << k)
                    node = node.left

        return mx

    def delete(self, num):
        s = bin(num)[2:].zfill(20)
        node = self.root

        for b in s:
            if b == '0':
                node.left_num -= 1
                node = node.left
            else:
                node.right_num -= 1
                node = node.right


class Solution:

    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        trie = Trie()
        j = 0
        ans = 0
        for i in range(0, n):
            while j < n and nums[j] <= 2 * nums[i]:
                trie.insert(nums[j])
                j += 1
            mx = trie.get_xor_max(nums[i])
            ans = max(mx, ans)
            trie.delete(nums[i])
        return ans


if __name__ == '__main__':
    sol = Solution()
    # nums = [10, 100]
    # nums = [1, 2, 3, 4, 5]
    nums = [500, 520, 2500, 3000]
    ret = sol.maximumStrongPairXor(nums)
    print(ret)
