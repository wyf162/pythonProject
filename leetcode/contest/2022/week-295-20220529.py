# _*_ coding: utf-8 _*_
# @Time : 2022/05/29 10:28 AM 
# @Author : yefe
# @File : week-295-20220529
from collections import Counter
from typing import List


class Solution:

    def rearrangeCharacters(self, s: str, target: str) -> int:
        cnt1 = Counter(s)
        cnt2 = Counter(target)
        ret = 100
        for k, v in cnt2.items():
            ret = min(ret, cnt1[k]//v)
        return ret

    def discountPrices(self, sentence: str, discount: int) -> str:
        words = sentence.split(' ')
        for i, word in enumerate(words):
            if word.startswith('$') and len(word)>1 and word[1:].isdigit():
                num = float(word[1:])
                num = num*(100-discount)/100
                words[i] = '${:.2f}'.format(num)
        return " ".join(words)

    def totalSteps(self, nums: List[int]) -> int:
        pass

    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        pass




if __name__ == '__main__':
    sol = Solution()
    sentence = "there are $1 $2 and 5$ candies in the shop"
    discount = 50
    ret = sol.discountPrices(sentence, discount)
    print(ret)
