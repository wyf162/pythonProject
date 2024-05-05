# -*- coding : utf-8 -*-
# @Time: 2024/5/5 10:30
# @Author: yefei.wang
# @File: a.py

class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) >= 3 and '@' not in word and '#' not in word and '$' not in word:
            word = word.lower()
            if any(c in word for c in 'aeiou') and any(c in word for c in 'bcdfghjklmnpqrstvwxyz'):
                return True
        return False
