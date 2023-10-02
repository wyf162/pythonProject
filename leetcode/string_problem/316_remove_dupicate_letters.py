# _*_ coding: utf-8 _*_
# @Time : 2022/05/25 8:53 PM 
# @Author : yefe
# @File : 316_remove_dupicate_letters
from collections import Counter
from string import ascii_lowercase


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        vis = {a: 0 for a in ascii_lowercase}
        cnt = Counter(s)
        print(cnt)
        stk = []
        for i in range(len(s)):
            if not vis[s[i]]:
                while stk and stk[-1] > s[i] and cnt[stk[-1]] > 0:
                    a = stk.pop()
                    vis[a] = 0
                stk.append(s[i])
                cnt[s[i]] -= 1
                vis[s[i]] = 1
            else:
                cnt[s[i]] -= 1
        return "".join(stk)


if __name__ == '__main__':
    sol = Solution()
    # s = "bcabc"
    # s = "cbacdcbc"
    s = "bbcaac"
    ret = sol.removeDuplicateLetters(s)
    print(ret)
