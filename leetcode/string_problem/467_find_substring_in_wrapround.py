# _*_ coding: utf-8 _*_
# @Time : 2022/05/25 8:02 PM 
# @Author : yefe
# @File : 467_find_substring_in_wrapround
from string import ascii_lowercase


class Solution:
    def findSubstringInWraproundString2(self, p: str) -> int:
        hst = {k: set() for k in ascii_lowercase}

        stk = []
        for i in range(len(p)):
            if not stk:
                stk.append(p[i])
            else:
                if self.is_continue(stk[-1], p[i]):
                    stk.append(p[i])
                else:
                    for j in range(len(stk)):
                        for k in range(len(stk)-j):
                            hst[stk[j]].add(k)
                    stk = [p[i]]
        for j in range(len(stk)):
            for k in range(len(stk) - j):
                hst[stk[j]].add(k)
        cnt = sum([len(x) for x in hst.values()])
        return cnt

    def findSubstringInWraproundString(self, p: str) -> int:
        hst = {k: 0 for k in ascii_lowercase}

        stk = []
        for i in range(len(p)):
            if not stk:
                stk.append(p[i])
            else:
                if self.is_continue(stk[-1], p[i]):
                    stk.append(p[i])
                else:
                    for j in range(len(stk)):
                        hst[stk[j]] = max(len(stk)-j, hst[stk[j]])
                    stk = [p[i]]
        for j in range(len(stk)):
            hst[stk[j]] = max(len(stk)-j, hst[stk[j]])
        cnt = sum([x for x in hst.values()])
        return cnt

    @staticmethod
    def is_continue(a, b):
        a = ord(a)-ord(b)
        return a in (-1, 25)


if __name__ == '__main__':
    sol = Solution()
    p = "zab"
    ret = sol.findSubstringInWraproundString(p)
    print(ret)

    # print(sol.is_continue('z', 'a'))
    # print(sol.is_continue('a', 'b'))
