# -*- coding : utf-8 -*-
# @Time: 2022/6/12 15:23
# @Author: yefei.wang
# @File: 6094_distinct_names.py
from typing import List
from collections import defaultdict
from itertools import product


class Solution:
    def distinctNames2(self, ideas: List[str]) -> int:
        group = defaultdict(int)
        for idea in ideas:
            group[idea[1:]] |= 1 << (ord(idea[0]) - ord('a'))

        ans = 0
        cnt = [[0]*26 for _ in range(26)]
        for mask in group.values():
            for i in range(26):
                if mask >> i & 1 == 0:
                    for j in range(26):
                        if mask >> j & 1:
                            cnt[i][j] += 1
                else:
                    for j in range(26):
                        if mask >> j & 1 == 0:
                            ans += cnt[i][j]
        return ans*2

    def distinctNames(self, ideas: List[str]) -> int:
        group = defaultdict(set)
        for idea in ideas:
            group[idea[0]].add(idea[1:])
        cnt = 0
        for a, b in product(group, repeat=2):
            if ord(a)<ord(b):
                cnt += (len(group[a])-len(group[a] & group[b]))*(len(group[b])-len(group[a] & group[b]))
        return cnt*2


if __name__ == '__main__':
    sol = Solution()
    ideas = ["coffee", "donuts", "time", "toffee"]
    ret = sol.distinctNames(ideas)
    print(ret)
