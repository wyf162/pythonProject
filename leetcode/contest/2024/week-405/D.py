# -*- coding : utf-8 -*-
# @Time: 2024/7/7 11:00
# @Author: yefei.wang
# @File: D.py

from typing import Sequence, List
from heapq import heappop, heappush

inf = 10 ** 18


def knuth_morris_pratt(text: Sequence, pattern: Sequence) -> List[int]:
    """
    Given two strings text and pattern, return the list of start indexes in text that matches with the pattern
    using knuth_morris_pratt algorithm.

    Args:
        text: Text to search
        pattern: Pattern to search in the text
    Returns:
        List of indices of patterns found

    Example:
        # >>> knuth_morris_pratt('hello there hero!', 'he')
        [0, 7, 12]

    If idx is in the list, text[idx : idx + M] matches with pattern.
    Time complexity of the algorithm is O(N+M), with N and M the length of text and pattern, respectively.
    """
    n = len(text)
    m = len(pattern)
    pi = [0 for i in range(m)]
    i = 0
    j = 0
    # making pi table
    for i in range(1, m):
        while j and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j
    # finding pattern
    j = 0
    ret = []
    for i in range(n):
        while j and text[i] != pattern[j]:
            j = pi[j - 1]
        if text[i] == pattern[j]:
            j += 1
            if j == m:
                ret.append(i - m + 1)
                j = pi[j - 1]
    return ret


class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        target = list(target)
        n = len(target)
        g = [[] for _ in range(n + 1)]

        for word, cost in zip(words, costs):
            nums = knuth_morris_pratt(target, word)
            for num in nums:
                g[num].append((num + len(word), cost))

        dis = [inf for _ in range(n + 1)]
        par = [-1 for _ in range(n + 1)]

        dis[0] = 0
        h = [(0, 0)]

        while h:
            d, x = heappop(h)
            if dis[x] < d:
                continue
            for y, w in g[x]:
                if d + w < dis[y]:
                    dis[y] = d + w
                    par[y] = x
                    heappush(h, (dis[y], y))

        return dis[-1] if dis[-1] < inf else -1


if __name__ == '__main__':
    sol = Solution()
    # target = "abcdef"
    # words = ["abdef", "abc", "d", "def", "ef"]
    # costs = [100, 1, 1, 10, 5]
    # ret = sol.minimumCost(target, words, costs)

    target = "aaaa"
    words = ["z", "zz", "zzz"]
    costs = [1, 10, 100]
    ret = sol.minimumCost(target, words, costs)
    print(ret)
