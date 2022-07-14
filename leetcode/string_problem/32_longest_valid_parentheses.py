# _*_ coding: utf-8 _*_
# @Time : 2022/4/10 上午8:59 
# @Author : wangyefei
# @File : 32_longest_valid_parentheses.py
import collections


class Solution:
    def longestValidParentheses2(self, s: str) -> int:
        pairs = set()
        stk = list()
        for idx, par in enumerate(s):
            if not stk:
                stk.append((idx, par))
            else:
                if par == '(':
                    stk.append((idx, par))
                else:
                    if stk[-1][1] == '(':
                        pidx, ppar = stk.pop()
                        pairs.add((pidx, idx))
                    else:
                        stk.append((idx, par))

        q = collections.deque()
        for pair in pairs:
            if pair[1]-pair[0]==1:
                q.append(pair)
        ret = 0
        while q:
            for _ in range(len(q)):
                s,t = q.popleft()
                if (s-1,t+1) in pairs:
                    q.append((s-1,t-1))
            ret += 2
        return ret

    def longestValidParentheses_v1(self, s: str) -> int:
        maxans = 0
        stk = list()
        stk.append(-1)
        for idx, par in enumerate(s):
            if par == '(':
                stk.append(idx)
            else:
                stk.pop()
                if not stk:
                    stk.append(idx)
                else:
                    maxans = max(maxans, idx - stk[-1])
        return maxans

    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0]*n
        for i in range(1,n):
            if s[i]==')':
                if s[i-1]=='(':
                    dp[i] = dp[i-2]+2 if i>=2 else 2
                elif i-dp[i-1]>0 and s[i-dp[i-1]-1]=='(':
                    dp[i] = dp[i-1]+2+dp[i - dp[i - 1] - 2] if i-dp[i-1]>=2 else dp[i-1]+2
        return max(dp)


if __name__ == '__main__':
    sol = Solution()
    s = "(()()))"
    ret = sol.longestValidParentheses(s)
    print(ret)



