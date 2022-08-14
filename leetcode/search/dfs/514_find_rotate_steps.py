# _*_ coding: utf-8 _*_
# @Time : 2022/08/13 6:34 PM 
# @Author : yefe
# @File : 514_find_rotate_steps
from functools import lru_cache


class Solution2:
    def findRotateSteps2(self, ring: str, key: str) -> int:

        @lru_cache(None)
        def dfs(ring, key, index):
            if index >= len(key):
                return 0

            res = 0
            # 找到所有能旋转的位置
            l_index = ring.find(key[index])

            min_val = []
            while l_index != -1:
                # 如果当前位置在字符串左半边，使用逆时针旋转 + 1 是拼写操作
                if l_index <= len(ring) // 2:
                    min_val.append(l_index + 1)
                else:
                    # 否则使用顺时针旋转
                    min_val.append(len(ring) - l_index + 1)
                # 获得旋转后的新表盘
                new_ring = ring[l_index:] + ring[:l_index]

                # 寻找下一个旋转点
                min_val[-1] += dfs(new_ring, key, index + 1)
                l_index = ring.find(key[index], l_index + 1)

            res = res + min(min_val) if min_val else 0
            return res

        return dfs(ring, key, 0)

    def findRotateSteps(self, ring: str, key: str) -> int:
        import collections, functools
        lookup = collections.defaultdict(list)
        for i in range(len(ring)):
            lookup[ring[i]].append(i)

        @lru_cache(None)
        def dfs(cur, k):
            if k == len(key):
                return 0
            res = float("inf")
            for j in lookup[key[k]]:
                res = min(res, min(tmp := abs(cur - j), len(ring) - tmp) + 1 + dfs(j, k + 1))
            return res

        return dfs(0, 0)


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:

        @lru_cache(None)
        def dfs(i, k):
            if i == len(key):
                return 0
            res = 10000
            for j in range(len(ring)):
                if ring[j] == key[i]:
                    rotate_step = min(abs(j-k), len(ring)-abs(j-k))
                    res = min(rotate_step+1+dfs(i + 1, j), res)
            return res

        return dfs(0, 0)


if __name__ == '__main__':
    sol = Solution()
    # ring = "godding"
    # key = "gd"
    # ring = "abcde"
    # key = "ade"
    ring = "caotmcaataijjxi"
    key = "oatjiioicitatajtijciocjcaaxaaatmctxamacaamjjx"
    ret = sol.findRotateSteps(ring, key)
    print(ret)
