# -*- coding : utf-8 -*-
# @Time: 2023/9/29 16:40
# @Author: yefei.wang
# @File: 720_longestWord.py

from collections import defaultdict, deque
from string import ascii_lowercase
from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        group = defaultdict(set)
        for word in words:
            group[len(word)].add(word)

        q = deque()
        for word in group.get(1, []):
            q.append(word)
        ans = list()
        l = 1
        while q:
            ans = list(q)
            for _ in range(len(q)):
                word = q.popleft()
                for c in ascii_lowercase:
                    if word+c in group[l+1]:
                        q.append(word+c)
        ans.sort()
        return ans[0]