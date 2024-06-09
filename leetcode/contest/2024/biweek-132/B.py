# -*- coding : utf-8 -*-
# @Time: 2024/6/8 22:55
# @Author: yefei.wang
# @File: B.py

from collections import deque, defaultdict
from typing import List


class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        q = deque()
        for i, x in enumerate(skills):
            q.append((i, x))

        cnt = defaultdict(int)
        n = len(skills)
        for i in range(n * 2):
            i1, x1 = q.popleft()
            i2, x2 = q.popleft()
            if x1 < x2:
                cnt[i2] += 1
                q.appendleft((i2, x2))
                q.append((i1, x1))
            else:
                cnt[i1] += 1
                q.appendleft((i1, x1))
                q.append((i2, x2))
            if cnt[i1] == k:
                ans = i1
                break
            elif cnt[i2] == k:
                ans = i2
                break
        else:
            ans = 0
            for k, v in cnt.items():
                if v > cnt[ans]:
                    ans = k
        return ans

