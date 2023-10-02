# -*- coding : utf-8 -*-
# @Time: 2022/1/5 22:29
# @Author: yefei.wang
# @File: 1576_modify_string.py
import random


class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)
        n = len(s)
        for i in range(n):
            if s[i]=='?':
                args = []
                if i-1>0:
                    args.append(s[i-1])
                if i+1<n:
                    args.append(s[i+1])
                s[i] = self.get(*args)
        return "".join(s)

    def get(self, *args):
        s = [i for i in range(ord('a'), ord('z')+1)]
        print(args)
        for arg in args:
            if ord(arg) in s:
                s.remove(ord(arg))
        print(s)
        c = chr(random.choice(s))
        return c


if __name__ == "__main__":
    s = "ubv?w"
    sol = Solution()
    # ans = sol.modifyString(s)
    # print(ans)
    ls = [chr(97+i) for i in range(25)]
    print(sol.get(*ls))
