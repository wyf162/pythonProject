# -*- coding : utf-8 -*-
# @Time: 2021/12/27 21:51
# @Author: yefei.wang
# @File: num_friend_requests.py
import math
from typing import List


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        hst = dict()
        for i in range(15, 100):
            hst[i] = [x for x in range(math.floor(0.5 * i + 7) + 1, i + 1)]
        for i in range(100, 121):
            hst[i] = [x for x in range(math.floor(0.5 * i + 7) + 1, i + 1)]
        cnt = dict()
        for age in ages:
            cnt[age] = cnt.get(age, 0) + 1
        ans = 0
        for k in ages:
            if k < 15:
                continue
            else:
                for y in hst.get(k, list()):
                    ans += cnt.get(y, 0)
                ans -= 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    ages = [
        109,
        6,
        101,
        18,
        13,
        20,
        106,
        110,
        110,
        108,
        55,
        89,
        81,
        56,
        84,
        37,
        71,
        51,
        88,
        70,
        27,
        16,
        31,
        63,
        99,
        68,
        12,
        120,
        104,
        18,
        110,
        42,
        93,
        106,
        99,
        63,
        3,
        82,
        22,
        17,
        69,
        49,
        88,
        117,
        57,
        37,
        95,
        15,
        50,
        18,
        77,
        103,
        102,
        104,
        87,
        1,
        23,
        97,
        93,
        15,
        9,
        35,
        59,
        103,
        118,
        23,
        52,
        66,
        86,
        7,
        40,
        33,
        60,
        4,
        113,
        43,
        21,
        58,
        31,
        120,
        71,
        56,
        19,
        67,
        68,
        32,
        84,
        14,
        50,
        55,
        98,
        34,
        89,
        32,
        58,
        20,
        93,
        37,
        95,
        40]
    ans = sol.numFriendRequests(ages)
    print(ans)
