# _*_ coding: utf-8 _*_
# @Time : 2022/08/21 3:04 PM 
# @Author : yefe
# @File : 6159_maximum_segment_sum

from typing import List


class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:

        n = len(nums)
        parent = [_ for _ in range(n)]
        rank = [0 for _ in range(n)]
        max_rank = 0

        ans = [0]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for query in removeQueries[::-1]:

            root = find(query)
            left, right = -1, -1
            if query < n - 1:
                right = find(query + 1)
            if query > 0:
                left = find(query - 1)

            rank[root] = nums[query]
            if left >= 0 and rank[left]:
                rank[root] += rank[left]
                parent[left] = root
            if right>=0 and rank[right]:
                rank[root] += rank[right]
                parent[right] = root

            max_rank = max(max_rank, rank[root])
            ans.append(max_rank)
        return ans[::-1][1:]


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 5, 6, 1]
    removeQueries = [0, 3, 2, 4, 1]
    ret = sol.maximumSegmentSum(nums, removeQueries)
    print(ret)

