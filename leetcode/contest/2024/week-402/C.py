# -*- coding : utf-8 -*-
# @Time: 2024/6/16 10:49
# @Author: yefei.wang
# @File: C.py
from collections import Counter
from typing import List


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        n = len(power)

        cnt = Counter(power)
        ks = list(sorted(cnt.keys()))
        m = len(ks)
        f = [0] * m
        for i in range(m):
            f[i] = ks[i] * cnt[ks[i]]
            if i - 1 >= 0 and ks[i] - ks[i - 1] > 2:
                f[i] = max(f[i], f[i - 1] + ks[i] * cnt[ks[i]])
            if i - 2 >= 0 and ks[i] - ks[i - 2] > 2:
                f[i] = max(f[i], f[i - 2] + ks[i] * cnt[ks[i]])
            if i - 3 >= 0 and ks[i] - ks[i - 3] > 2:
                f[i] = max(f[i], f[i - 3] + ks[i] * cnt[ks[i]])
            f[i] = max(f[i], f[i - 1])
        ret = max(f)
        return ret


if __name__ == '__main__':
    sol = Solution()
    power = [2, 1, 4, 3, 1, 1, 1, 5]
    ret = sol.maximumTotalDamage(power)
    print(ret)
