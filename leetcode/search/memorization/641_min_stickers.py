# _*_ coding: utf-8 _*_
# @Time : 2022/05/14 4:19 PM 
# @Author : yefe
# @File : 641_min_stickers
from functools import cache
from typing import List
from collections import defaultdict, Counter
from copy import deepcopy


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        m = len(target)

        @cache
        def dfs(mask: int) -> int:
            if mask == 0:
                return 0
            res = m + 1
            for sticker in stickers:
                left = mask
                cnt = Counter(sticker)
                for i, c in enumerate(target):
                    if mask >> i & 1 and cnt[c]:
                        cnt[c] -= 1
                        left ^= 1 << i
                if left < mask:
                    res = min(res, dfs(left) + 1)
            return res

        res = dfs((1 << m) - 1)
        return res


if __name__ == '__main__':
    sol = Solution()
    stickers = ["with", "example", "science"]
    target = "thehat"
    ret = sol.minStickers(stickers, target)
    print(ret)
