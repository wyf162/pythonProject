# _*_ coding: utf-8 _*_
# @Time : 2022/4/17 下午10:29 
# @Author : wangyefei
# @File : 819_most_common_word.py
from collections import defaultdict
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        paragraph += " "
        i, n = 0, len(paragraph)
        hst = defaultdict(int)

        word = ""
        for i in range(n):
            if paragraph[i].isalpha():
                word += paragraph[i].lower()
            else:
                if word and word not in banned:
                    hst[word] += 1
                word = ""

        target_count = max(hst.values())
        for k, v in hst.items():
            if v==target_count:
                return k


if __name__ == '__main__':
    sol = Solution()
    paragraph = "Bob"
    banned = ["hit"]
    ret = sol.mostCommonWord(paragraph, banned)
    print(ret)
