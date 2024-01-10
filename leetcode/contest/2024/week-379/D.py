# -*- coding : utf-8 -*-
# @Time: 2024/1/7 10:31
# @Author: yefei.wang
# @File: D.py

from collections import Counter


class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        modify = 1
        hst = Counter()
        ans = 0
        cnt = 0
        for c in s:
            hst[c] += 1
            cnt += 1
            if len(hst) == k:
                ans += 1
                modify += 1
                hst = Counter()
                cnt = 0
            elif cnt >= k and cnt - len(hst) <= modify:
                ans += 1
                modify += 1
                hst = Counter()
                cnt = 0
                modify -= k - len(hst)
        if cnt:
            ans += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    # s = "accca"
    # k = 2
    s = "aabaab"
    k = 3
    ret = sol.maxPartitionsAfterOperations(s, k)
    print(ret)
