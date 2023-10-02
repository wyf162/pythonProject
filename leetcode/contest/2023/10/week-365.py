# -*- coding : utf-8 -*-
# @Time: 2023/10/1 10:25
# @Author: yefei.wang
# @File: week-365.py
from collections import Counter, deque
from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        lmx = [0] * n
        lmx[0] = nums[0]
        for i in range(1, n):
            lmx[i] = max(lmx[i - 1], nums[i])

        rmx = [0] * n
        rmx[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            rmx[i] = max(rmx[i + 1], nums[i])

        ans = float('-inf')
        for j in range(1, n - 1):
            ans = max(ans, (lmx[j - 1] - nums[j]) * rmx[j + 1])
        return ans if ans >= 0 else 0

    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        n = len(nums)
        s = sum(nums)
        x, y = divmod(target, s)
        if y == 0:
            return x * n

        cnt = Counter()
        pre_sum = [0] * (2 * n + 1)
        cnt[0] = -1
        ans = float('inf')
        nn = nums + nums
        for i in range(2 * n):
            pre_sum[i + 1] = pre_sum[i] + nn[i]
            diff = pre_sum[i + 1] - y
            if diff in cnt and i - cnt[diff] <= n:
                ans = min(ans, i - cnt[diff])
                print(i, cnt[diff])
            cnt[pre_sum[i + 1]] = i

        ans = x * n + ans
        return ans if ans < float('inf') else -1

    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        n = len(edges)
        g = [[] for _ in range(n)]
        in_deg = [0 for _ in range(n)]
        out_deg = [0 for _ in range(n)]
        for u, v in enumerate(edges):
            g[u].append(v)
            in_deg[v] += 1
            out_deg[u] += 1

        q = deque()
        for i in range(n):
            if in_deg[i] == 0:
                q.append(i)

        to_circle = set()
        in_circle = set()
        circle_to = set()

        while q:
            x = q.popleft()
            to_circle.add(x)
            for y in g[x]:
                in_deg[y] -= 1
                if in_deg[y] == 0:
                    q.append(y)
        for i in range(n):
            pass


if __name__ == '__main__':
    sol = Solution()
    # nums = [2, 3, 5, 2, 3, 4, 4, 1, 3, 5, 2, 2, 5, 1, 1, 2, 5]
    # target = 19
    nums = [1, 6, 5, 5, 1, 1, 2, 5, 3, 1, 5, 3, 2, 4, 6, 6]
    target = 56
    ret = sol.minSizeSubarray(nums, target)
    print(ret)
