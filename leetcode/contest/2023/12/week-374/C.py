# -*- coding : utf-8 -*-
# @Time: 2023/12/3 10:29
# @Author: yefei.wang
# @File: C.py
import bisect


def idx(c):
    return ord(c) - ord('a')


class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        g = [[-1] for i in range(26)]
        for i in range(n):
            g[idx(word[i])].append(i)
        cnt = [0] * 26
        for i in range(n):
            cnt[idx(word[i])] += 1
            j = cnt[idx(word[i])]
            if j >= k:
                prev = g[j - k]
                for c in range(26):
                    left = bisect.insort_left(g[i], prev)
                    right = bisect.bisect_right(g[i], i)



if __name__ == '__main__':
    sol = Solution()
    # word = "eebb"
    # k = 2
    word = "baab"
    k = 2
    ret = sol.countCompleteSubstrings(word, k)
    print(ret)
