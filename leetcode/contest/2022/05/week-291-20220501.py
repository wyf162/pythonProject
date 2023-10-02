# _*_ coding: utf-8 _*_
# @Time : 2022/05/00 10:29 AM
# @Author : yefe
# @File : week-300-20220501
import collections
from typing import List
from collections import defaultdict


class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        n = len(number)
        target = []
        for i in range(n):
            if number[i] == digit:
                target.append(int(number[:i] + number[i + 1:]))
        return str(max(target))

    def minimumCardPickup(self, cards: List[int]) -> int:
        hst = dict()
        ret = len(cards) + 2
        for i, card in enumerate(cards):
            if card not in hst:
                hst[card] = i
            else:
                ret = min(ret, i - hst[card] + 1)
                hst[card] = i

        if ret == len(cards) + 2:
            return -1
        else:
            return ret

    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        n = len(nums)
        cnt = [0] * (n + 1)
        for i in range(n):
            if nums[i] % p == 0:
                cnt[i + 1] = cnt[i] + 1
            else:
                cnt[i + 1] = cnt[i]
        print(cnt)
        visited = set()
        for i in range(n):
            visited.add(tuple(nums[i:i + 1]))
            for j in range(i + 1, n):
                if cnt[j + 1] - cnt[i] <= k:
                    visited.add(tuple(nums[i:j + 1]))
        print(visited)
        return len(visited)

    def appealSum(self, s: str) -> int:
        c2i = collections.defaultdict(lambda: [-1])
        for i, t in enumerate(s):
            c2i[t].append(i)
        for k in c2i:
            c2i[k].append(len(s))
        to_ret = 0
        # print(dict(c2i))
        for c in c2i:
            vt = c2i[c]
            for i in range(1, len(vt) - 1):
                to_ret += (vt[i] - vt[i - 1]) * (len(s) - vt[i])
            # print(c, to_ret)
        return to_ret


if __name__ == '__main__':
    sol = Solution()
    s = "abbca"
    ret = sol.appealSum(s)
    print(ret)

    # nums = [2,3,2,3,2]
    # nums = [2, 3, 3, 2, 2]
    # nums = [1, 2, 3, 4]
    # k = 4
    # p = 1
    # ret = sol.countDistinct(nums, k, p)
    # print(ret)

    # cards = [3, 4, 2, 3, 4, 7]
    # cards = [1, 1]
    # ret = sol.minimumCardPickup(cards)
    # print(ret)
    # number = "4541"
    # digit = "4"
    # ret = sol.removeDigit(number, digit)
    # print(ret)
