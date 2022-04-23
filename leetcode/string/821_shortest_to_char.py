# _*_ coding: utf-8 _*_
# @Time : 2022/4/19 下午6:53 
# @Author : wangyefei
# @File : 821_shortest_to_char.py
from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        res = [None] * n
        pre = None
        for i in range(n):
            if s[i]==c:
                pre = i
                res[i]=0
            if pre is not None:
                res[i] = i-pre
        pre = None
        for i in range(n-1,-1,-1):
            if s[i]==c:
                pre = i
                res[i] = 0
            if pre is not None:
                if res[i]:
                    res[i] = min(res[i], pre-i)
                else:
                    res[i] = pre-i
        return res


if __name__ == '__main__':
    sol = Solution()
    # s = "loveleetcode"
    # c = "e"
    s="baaa"
    c="b"
    # [3,2,1,0,1,0,0,1,2,2,1,0]
    ret = sol.shortestToChar(s, c)
    print(ret)