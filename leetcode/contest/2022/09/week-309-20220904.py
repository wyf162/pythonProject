# _*_ coding: utf-8 _*_
# @Time : 2022/09/04 10:30 AM 
# @Author : yefe
# @File : week-309-20220904


from typing import List
from math import comb
import heapq
from collections import Counter


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        hst = dict()
        for i, a in enumerate(s):
            if a not in hst:
                hst[a] = i
            else:
                d = i - hst[a] - 1
                idx = ord(a) - ord('a')
                if distance[idx] == d:
                    continue
                else:
                    return False
        return True

    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        d = abs(endPos - startPos)
        if k < d:
            return 0
        elif (k - d) % 2 == 1:
            return 0
        else:
            t = (k - d) // 2
            return comb(k, t) % MOD

    def longestNiceSubarray(self, nums: List[int]) -> int:
        bits = [0] * 30
        n = len(nums)
        i, j = 0, 0
        ans = 0
        while j < n:
            num = nums[j]

            for k in range(30):
                if num & (1 << k):
                    bits[k] += 1
            j += 1

            while bits.count(2):
                num = nums[i]
                for k in range(30):
                    if num & (1 << k):
                        bits[k] -= 1
                i += 1
            ans = max(ans, j - i)
        return ans

    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:

        valid_room = [i for i in range(n)]
        heapq.heapify(valid_room)

        meetings.sort()

        record = []
        heapq.heapify(record)

        cnt = [-1] * (len(meetings))

        ts = 0
        for i, meeting in enumerate(meetings):
            ts = meeting[0]
            while record and record[0][0] <= ts:
                _, room_number = heapq.heappop(record)
                heapq.heappush(valid_room, room_number)

            if valid_room:
                room_number = heapq.heappop(valid_room)
                heapq.heappush(record, (ts + meeting[1] - meeting[0], room_number))
                cnt[i] = room_number
            else:
                ts, room_number = heapq.heappop(record)
                heapq.heappush(record, (ts + meeting[1] - meeting[0], room_number))
                cnt[i] = room_number

        # print(cnt)

        counter = Counter(cnt)
        max_freq = max(counter.values())
        for i in range(n):
            if counter[i] == max_freq:
                return i


if __name__ == '__main__':
    sol = Solution()
    # n = 2
    # meetings = [[0, 10], [1, 5], [2, 7], [3, 4]]
    # n = 3
    # meetings = [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]
    n= 4
    meetings = [[48, 49], [22, 30], [13, 31], [31, 46], [37, 46], [32, 36], [25, 36], [49, 50], [24, 34], [6, 41]]
    ret = sol.mostBooked(n, meetings)
    print(ret)

    # nums = [1, 3, 8, 48, 10]
    # ret = sol.longestNiceSubarray(nums)
    # print(ret)
