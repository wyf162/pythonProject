# -*- coding: utf-8 -*-
# @Time: 2024/3/13 13:38
# @Author: yfwang
# @File: 3076.py

from typing import List


class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:

        n = len(arr)
        ans = [None for _ in range(n)]
        for i in range(n):

            s = arr[i]
            m = len(s)
            for i1 in range(m):
                for i2 in range(i1+1, m+1):
                    t = s[i1:i2]
                    tag = True
                    for j in range(n):
                        if i == j:
                            continue
                        if t in arr[j]:
                            tag = False
                            break
                    if tag:
                        if ans[i] is not None:
                            if len(t) < len(ans[i]):
                                ans[i] = t
                            elif len(t) == len(ans[i]):
                                ans[i] = min(ans[i], t)
                        else:
                            ans[i] = t
        for i in range(n):
            if ans[i] is None:
                ans[i] = ""
        return ans


if __name__ == '__main__':
    sol = Solution()
    arr = ["cab", "ad", "bad", "c"]
    ret = sol.shortestSubstrings(arr)
    print(ret)
