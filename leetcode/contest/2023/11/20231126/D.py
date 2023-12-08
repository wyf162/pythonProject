# -*- coding : utf-8 -*-
# @Time: 2023/11/26 10:44
# @Author: yefei.wang
# @File: D.py
from collections import defaultdict, Counter


class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        a = 1
        while True:
            if a * a % k == 0:
                break
            else:
                a += 1

        n = len(s)
        group = defaultdict(list)
        cur = 0
        group[0] .append(0)
        for i in range(n):
            if s[i] in 'aeiou':
                cur += 1
            else:
                cur -= 1
            group[cur].append(i+1)

        ans = 0
        for _, idxs in group.items():
            cnt = Counter()
            for i in idxs:
                k = i % (a * 2)
                ans += cnt[k]
                cnt[k] += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    s = 'bcdf'
    k = 1
    ret = sol.beautifulSubstrings(s, k)
    print(ret)
