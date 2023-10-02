# -*- coding : utf-8 -*-
# @Time: 2023/9/29 18:50
# @Author: yefei.wang
# @File: 316_removeDuplicateLetters.py

from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        cnt = Counter(s)
        stk = []
        n = len(s)
        for i in range(n):
            if s[i] in stk:
                cnt[s[i]] -= 1
                continue
            while stk and stk[-1] > s[i] and cnt[stk[-1]] > 0:
                stk.pop()
            stk.append(s[i])
            cnt[s[i]] -= 1
        return ''.join(stk)


if __name__ == '__main__':
    sol = Solution()
    s = "bbcaac"
    ret = sol.removeDuplicateLetters(s)
    print(ret)
