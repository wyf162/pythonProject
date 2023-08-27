# _*_ coding: utf-8 _*_
# @Time : 2022/11/13 10:35 AM 
# @Author : yefe
# @File : week-319-20221113

from collections import deque
from typing import List, Optional
from math import lcm

from leetcode.tree.tree_utils import TreeNode


class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ret = 0
        for i in range(n):
            t = nums[i]
            for j in range(i, n):
                t = lcm(t, nums[j])
                if t == k:
                    ret += 1
                elif k % t != 0:
                    break
        return ret

    def minimumOperations(self, root: Optional[TreeNode]) -> int:

        def helper(nums: List[int]) -> int:
            n = len(nums)
            snums = sorted(nums)
            mp = dict()
            for i, num in enumerate(nums):
                mp[num] = i
            loops = 0
            flags = [False] * n

            for i in range(n):
                if not flags[i]:
                    j = i
                    while not flags[j]:
                        j = mp.get(snums[j])
                        flags[j] = True
                    loops += 1
            return n - loops

        q = deque()
        q.append(root)
        ret = 0
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ret += helper(level)
        return ret


if __name__ == '__main__':
    sol = Solution()
    # nums = [1]*1000
    # k = 1
    nums = [3, 6, 2, 7, 1]
    k = 6
    ret = sol.subarrayLCM(nums, k)
    print(ret)
