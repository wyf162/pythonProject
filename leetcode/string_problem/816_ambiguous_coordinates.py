# _*_ coding: utf-8 _*_
# @Time : 2022/11/07 8:33 PM 
# @Author : yefe
# @File : 816_ambiguous_coordinates

from typing import List


class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        rets = []
        n = len(s)
        for i in range(1, n - 1):
            ls = self.partition(s[1:i])
            rs = self.partition(s[i:-1])
            for l in ls:
                for r in rs:
                    if l and r:
                        rets.append('(' + l + ', ' + r + ')')
        return rets

    @staticmethod
    def partition(s: str) -> List[str]:
        rets = []
        if s.startswith('0'):
            if len(s) == 1:
                rets.append(s)
            elif len(s) > 1 and len(set(list(s))) > 1 and s[-1]!='0':
                rets.append(s[:1] + '.' + s[1:])

        else:
            rets.append(s)
            for i in range(1, len(s)):
                if s[-1] == '0':
                    break
                rets.append(s[:i] + '.' + s[i:])
        return rets


if __name__ == '__main__':
    sol = Solution()
    # s = "(123)"
    # s = "(100)"
    s = "(0010)"
    rets = sol.ambiguousCoordinates(s)
    print(rets)
