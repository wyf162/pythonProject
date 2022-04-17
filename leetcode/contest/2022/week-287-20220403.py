# _*_ coding: utf-8 _*_
# @Time : 2022/4/3 上午10:26 
# @Author : wangyefei
# @File : week-287-20220403.py
from typing import List
from collections import Counter


class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        hour = int(correct[:2]) - int(current[:2])
        minute = int(correct[3:]) - int(current[3:])
        minutes = hour * 60 + minute
        ret = 0
        while minutes > 0:
            if minutes >= 60:
                minutes -= 60
            elif minutes >= 15:
                minutes -= 15
            elif minutes >= 5:
                minutes -= 5
            else:
                minutes -= 1
            ret += 1
        return ret

    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win_hst = dict()
        # defeat
        dft_hst = dict()
        for match in matches:
            winner, loser = match
            win_hst[winner] = win_hst.get(winner, 0) + 1
            dft_hst[loser] = dft_hst.get(loser, 0) + 1

        ret_0 = []
        for winner in win_hst.keys():
            if dft_hst.get(winner, 0) == 0:
                ret_0.append(winner)
        ret_0.sort()

        ret_1 = []
        for loser in dft_hst.keys():
            if dft_hst.get(loser) == 1:
                ret_1.append(loser)

        ret_1.sort()
        return [ret_0, ret_1]

    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        l = 1
        r = max(candies)
        while l <= r:
            mid = (l + r) >> 1
            # print(l, r, mid)
            # print(mid)
            if self.check(candies, k, mid):
                l = mid + 1
            else:
                r = mid - 1
            # print(l, r, mid)
        return r

    def check(self, candies, k, n):
        return sum([candy // n for candy in candies]) >= k


class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.encrypt_hst = {key: val for key, val in zip(keys, values)}
        self.hst = dict(Counter(dictionary))
        self.decrypt_hst = {val: list() for val in values}
        for key, val in zip(keys, values):
            self.decrypt_hst[val].append(key)

        self.new_hst = dict()
        for key, val in self.hst.items():
            new_str = self.encrypt(key)
            self.new_hst[new_str] = self.new_hst.get(new_str, 0) + val

    def encrypt(self, word1: str) -> str:
        ret = ""
        for w in word1:
            ret += self.encrypt_hst[w]
        return ret

    def decrypt(self, word2: str) -> int:
        return self.new_hst[word2]

    # def decrypt(self, word2: str) -> int:
    #     ret = ""
    #     for i in range(0, len(word2), 2):
    #         ret += self.decrypt_hst[word2[i:i + 2]][0]
    #     print(ret)
    #     return self.hst.get(ret, 0)

    # def decrypt(self, word2: str) -> int:
    #     self.ret = 0
    #
    #     def dfs(i, s):
    #         if i == len(word2):
    #             self.ret += self.hst.get(s, 0)
    #         else:
    #             for w in self.decrypt_hst.get(word2[i:i + 2], list()):
    #                 dfs(i + 2, s + w)
    #
    #     dfs(0, "")
    #     return self.ret


if __name__ == '__main__':
    keys = ['a', 'b', 'c', 'd']
    values = ["ei", "zf", "ei", "am"]
    dictionary = ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"]
    encrypter = Encrypter(keys, values, dictionary)
    word1 = "abcd"
    ret = encrypter.encrypt(word1)
    print(ret)
    word2 = "eizfeiam"
    ret = encrypter.decrypt(word2)
    print(ret)

    # sol = Solution()
    # candies = [5, 8, 6]
    # k = 90
    # ret = sol.maximumCandies(candies, k)
    # print(ret)

    # matches = [[2, 3], [1, 3], [5, 4], [6, 4]]
    # matches = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]
    # ret = sol.findWinners(matches)
    # print(ret)
