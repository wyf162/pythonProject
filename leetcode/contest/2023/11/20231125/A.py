# -*- coding : utf-8 -*-
# @Time: 2023/11/25 22:27
# @Author: yefei.wang
# @File: B.py


from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, word in enumerate(words) if x in word]