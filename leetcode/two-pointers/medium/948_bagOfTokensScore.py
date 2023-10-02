# -*- coding : utf-8 -*-
# @Time: 2023/9/30 18:07
# @Author: yefei.wang
# @File: 948_bagOfTokensScore.py

import collections


class Solution(object):
    def bagOfTokensScore(self, tokens, P):
        tokens.sort()
        deque = collections.deque(tokens)
        ans = bns = 0
        while deque and (P >= deque[0] or bns):
            while deque and P >= deque[0]:
                P -= deque.popleft()
                bns += 1
            ans = max(ans, bns)

            if deque and bns:
                P += deque.pop()
                bns -= 1

        return ans


if __name__ == '__main__':
    sol = Solution()
    # tokens = [100]
    # power = 50
    tokens = [71, 55, 82]
    power = 54
    ret = sol.bagOfTokensScore(tokens, power)
    print(ret)
