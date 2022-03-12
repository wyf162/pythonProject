# _*_ coding: utf-8 _*_
# @Time : 2022/3/8 下午9:49 
# @Author : wangyefei
# @File : 2055_plates_between_candles.py
from typing import List


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        left = [0 for _ in range(n)]
        right = [n - 1 for _ in range(n)]
        t = -1
        for i in range(n):
            if s[i] == '|':
                t = i
            left[i] = t
        t = n
        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                t = i
            right[i] = t
        pre = [0]
        for i in range(n):
            if s[i] == '*':
                pre.append(pre[-1] + 1)
            else:
                pre.append(pre[-1])
        ans = list()
        for query in queries:
            l = left[query[1]]
            r = right[query[0]]
            cnt = pre[l] - pre[r] if l > r else 0
            ans.append(cnt)
        return ans


if __name__ == '__main__':
    sol = Solution()
    # s = "**|**|***|"
    # queries = [[2, 5], [5, 9], [3, 9], [1, 9]]
    s = "***|**|*****|**||**|*"
    queries = [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]
    # s = "*|*|||"
    # queries = [[0, 0], [1, 3]]
    ret = sol.platesBetweenCandles(s, queries)
    print(ret)
