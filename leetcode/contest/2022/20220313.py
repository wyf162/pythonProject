# _*_ coding: utf-8 _*_
# @Time : 2022/3/13 上午10:31 
# @Author : wangyefei
# @File : 20220313.py
import collections
from typing import List
from heapq import heappush, heappop


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        ret = set()
        for idx, num in enumerate(nums):
            if num == key:
                for i in range(-1 * k, k + 1, 1):
                    if 0 <= idx + i < n:
                        ret.add(idx + i)
        return sorted(list(ret))

    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        artifact_count = len(artifacts)
        grid = [[-1 for j in range(n)] for i in range(n)]
        cnt = [0 for _ in range(artifact_count)]
        for idx, artifact in enumerate(artifacts):
            r1, c1, r2, c2 = artifact
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    grid[i][j] = idx
                    cnt[idx] += 1
        # print(grid)
        grid_dig = [[-1 for j in range(n)] for i in range(n)]
        for i, j in dig:
            grid_dig[i][j] = -2
        # print(grid_dig)
        # print(cnt)
        for i in range(n):
            for j in range(n):
                idx = grid[i][j]
                if idx >= 0 and grid_dig[i][j] == -2:
                    cnt[idx] -= 1
        # print(cnt)
        ret = 0
        for idx in range(artifact_count):
            if cnt[idx] == 0:
                ret += 1
        return ret

    def maximumTop2(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k > len(nums):
            return max(nums)
        hst = dict(collections.Counter(nums))
        s1 = set()
        sn = set()
        for key, val in hst.items():
            if val == 1:
                s1.add(key)
            else:
                sn.add(key)

        i = 0
        while i < n:
            if nums[i] in s1:
                break
            else:
                hst[nums[i]] -= 1
                if hst[nums[i]] == 0:
                    break
        # 大于marked_idx 可插入和可弹出
        marked_idx = i
        ret = -1
        can_insert_max = -1
        for i in range(k):
            if nums[i] in s1:
                can_insert_max = max(can_insert_max, nums[i])
            else:
                hst[nums[i]] -= 1
                if hst[nums[i]] == 0:
                    can_insert_max = max(can_insert_max, nums[i])
            if i >= marked_idx and (k - i) % 2 == 0:
                ret = max(ret, can_insert_max)

        return ret

    def maximumTop(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if len(nums) == 1 and k % 2 == 1:
            return -1
        if k > len(nums):
            return max(nums)
        ret = -1
        can_insert_max = -1
        for i in range(k):
            can_insert_max = max(can_insert_max, nums[i])
            if (k - i) % 2 == 0:
                ret = max(ret, can_insert_max)
        if k < n:
            ret = max(ret, nums[k])

        return ret

    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        fnes, bnes = [[] for _ in range(n)], [[] for _ in range(n)]
        dist1, dist2, dist3 = [10 ** 15] * n, [10 ** 15] * n, [10 ** 15] * n

        for f, t, w in edges:
            fnes[f].append((t, w))
            bnes[t].append((f, w))

        def dijkstra(s, nes, dist):
            h = []
            dist[s] = 0
            heappush(h, (0, s))
            while len(h):
                cost, node = heappop(h)
                if cost > dist[node]:
                    continue
                for ne, w in nes[node]:
                    if cost + w < dist[ne]:
                        dist[ne] = cost + w
                        heappush(h, (cost + w, ne))

        dijkstra(src1, fnes, dist1)
        dijkstra(src2, fnes, dist2)
        dijkstra(dest, bnes, dist3)

        res = 10 ** 15
        for i in range(n):
            res = min(res, dist1[i] + dist2[i] + dist3[i])

        return res


if __name__ == '__main__':
    sol = Solution()
    n = 6
    edges = [[0, 2, 2], [0, 5, 6], [1, 0, 3], [1, 4, 5], [2, 1, 1], [2, 3, 3], [2, 3, 4], [3, 4, 2],
                    [4, 5, 1]]
    src1 = 0
    src2 = 1
    dest = 5

    ret = sol.minimumWeight(n, edges, src1, src2, dest)
    print(ret)

    # nums = [52, 78, 54, 87, 34, 7, 17, 75, 89, 34, 38, 99, 78, 91, 28, 83, 96, 89, 22, 70, 88, 11, 41, 54, 17, 90,
    # 26, 33, 74, 40, 5, 78, 5, 14, 82, 34, 16, 77, 36, 36, 100, 71, 60, 98, 73, 38, 69, 59, 45, 100, 25, 72, 11, 31,
    # 88, 41, 33, 29, 3, 92, 51, 80]  # 99 k = 34 nums = [5,2,2,4,0,6] k = 7 nums = [1,2,7,1,2,0] k = 5 nums = [31,
    # 15, 92, 84, 19, 92, 55]   # 92 k = 4 nums = [35, 43, 23, 86, 23, 45, 84, 2, 18, 83, 79, 28, 54, 81, 12, 94, 14,
    # 0, 0, 29, 94, 12, 13, 1, 48, 85, 22, 95, 24, 5, 73, 10, 96, 97, 72, 41, 52, 1, 91, 3, 20, 22, 41, 98, 70, 20,
    # 52, 48, 91, 84, 16, 30, 27, 35, 69, 33, 67, 18, 4, 53, 86, 78, 26, 83, 13, 96, 29, 15, 34, 80, 16, 49]  # 94 k
    # = 15 nums = [2, 3] k = 2 nums = [91, 98, 17, 79, 15, 55, 47, 86, 4, 5, 17, 79, 68, 60, 60, 31, 72, 85, 25, 77,
    # 8, 78, 40, 96, 76, 69, 95, 2, 42, 87, 48, 72, 45, 25, 40, 60, 21, 91, 32, 79, 2, 87, 80, 97, 82, 94, 69, 43,
    # 18, 19, 21, 36, 44, 81, 99] k = 2
    # ret = sol.maximumTop(nums, k)
    # print(ret)

    # n = 2
    # artifacts = [[0, 0, 0, 0], [0, 1, 1, 1]]
    # dig = [[0, 0], [0, 1]]
    # n = 2
    # artifacts = [[0, 0, 0, 0], [0, 1, 1, 1]]
    # dig = [[0, 0], [0, 1], [1, 1]]
    # ret = sol.digArtifacts(n, artifacts, dig)
    # print(ret)
    # nums = [3, 4, 9, 1, 3, 9, 5]
    # key = 9
    # k = 1
    # ret = sol.findKDistantIndices(nums, key, k)
    # print(ret)
