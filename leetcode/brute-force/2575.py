# -*- coding: utf-8 -*-
# @Time: 2024/3/7 15:50
# @Author: yfwang
# @File: 2575.py
from typing import List


class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        n = len(word)
        div = [0] * n
        x = 0
        for i in range(n):
            x = x * 10 + int(word[i])
            x = x % m
            if x == 0:
                div[i] = 1
        return div


if __name__ == '__main__':
    sol = Solution()
    word = "998244353"
    m = 3
    ret = sol.divisibilityArray(word, m)
    print(ret)
