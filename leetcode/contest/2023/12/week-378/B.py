# -*- coding : utf-8 -*-
# @Time: 2023/12/31 10:33
# @Author: yefei.wang
# @File: B.py

from collections import defaultdict


class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        hst = defaultdict(list)
        cnt = 1
        for i in range(1, n):
            if s[i] == s[i - 1]:
                cnt += 1
            else:
                hst[s[i - 1]].append(cnt)
                cnt = 1
        hst[s[n - 1]].append(cnt)

        rst = -1
        for k, v in hst.items():
            v.sort(reverse=True)
            if len(v) >= 3 and v[0] == v[2]:
                rst = max(rst, v[0])
            if len(v) >= 2 and v[1] >= 1 and v[0] - v[1] <= 1:
                rst = max(rst, v[0] - 1)
            if v[0] > 2:
                rst = max(rst, v[0] - 2)
        return rst if rst > 0 else -1


if __name__ == '__main__':
    sol = Solution()
    s = 'ada'
    ret = sol.maximumLength(s)
    print(ret)
