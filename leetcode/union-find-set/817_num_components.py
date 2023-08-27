# _*_ coding: utf-8 _*_
# @Time : 2022/10/12 8:51 PM 
# @Author : yefe
# @File : 817_num_components
from collections import defaultdict, deque
from typing import Optional, List


class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    @classmethod
    def init_from_list(cls, nums):
        begin = ListNode(nums[0])
        cur = begin
        for i in range(1, len(nums)):
            cur.next = ListNode(nums[i])
            cur = cur.next
        return begin


class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        hst = defaultdict(list)

        pre = head
        cur = head.next
        while cur:
            hst[pre.val].append(cur.val)
            hst[cur.val].append(pre.val)
            pre = cur
            cur = cur.next

        cnt = 0
        vis = set()
        all = set(nums)

        for num in nums:
            if num not in vis:
                cnt += 1
                q = deque()
                q.append(num)
                vis.add(num)
                while q:
                    v = q.popleft()
                    for n in hst[v]:
                        if n not in vis and n in all:
                            q.append(n)
                            vis.add(n)
        return cnt


if __name__ == '__main__':
    head = ListNode.init_from_list([0,1,2,3])
    nums = [0,1,3]
    sol = Solution()
    ret = sol.numComponents(head, nums)
    print(ret)


