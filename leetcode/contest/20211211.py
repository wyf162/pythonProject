# -*- coding : utf-8 -*-
# @Time: 2021/12/11 22:11
# @Author: yefei.wang
# @File: 20211211.py
from typing import List
import heapq
import math
import collections


class Solution:

    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        s_nums = sorted(nums)
        print(s_nums)
        pivot = s_nums[n-k]
        c = 0
        for i in range(n-k,n):
            if s_nums[i]==pivot:
                c += 1
            else:
                break
        print(pivot, c)
        ans = []
        for num in nums:
            if num>pivot:
                ans.append(num)
            elif num==pivot and c>0:
                ans.append(num)
                c -= 1
        return ans

    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        non_increase = [0]*n
        for i in range(1,n):
            if security[i]<=security[i-1]:
                non_increase[i] = non_increase[i-1]+1

        non_decrease = [0]*n
        for i in range(n-2,0,-1):
            if security[i]<=security[i+1]:
                non_decrease[i] = non_decrease[i+1]+1
        ans = []
        for i in range(n):
            if non_decrease[i]>=time and non_increase[i]>=time:
                ans.append(i)
        return ans

    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        # adj_matrix = [[0 for j in range(n)] for i in range(n)]
        adj_tbl = collections.defaultdict(list)


        for i in range(n):
            for j in range(i+1,n):
                if self.check(bombs[i], bombs[j]):
                    print(i,j)
                    adj_tbl[i].append(j)
                if self.check(bombs[j], bombs[i]):
                    print(j,i)
                    adj_tbl[j].append(i)
                    # adj_matrix[i][j] = 1
                    # adj_matrix[j][i] = 1
        ans = 0

        for i in range(n):
            unvisited = [True] * n
            dq = []
            dq.append(i)
            unvisited[i] = False
            cnt = 0
            while dq:
                v = dq.pop(0)
                cnt += 1
                for u in adj_tbl[v]:
                    if unvisited[u]:
                        dq.append(u)
                        unvisited[u] = False

            ans = max(ans,cnt)
        return ans

    def check(self, bomb1, bomb2):
        x1,y1,r1 = bomb1
        x2,y2,r2 = bomb2
        d = math.sqrt((x1-x2)**2+(y1-y2)**2)
        r = r1
        return d<=r


class SORTracker:

    def __init__(self):
        self.insights = []
        self.idx = -1

    def add(self, name: str, score: int) -> None:
        cur_sight = [name, score]
        if self.insights:
            i = 0
            while i < len(self.insights):
                if self.cmp(self.insights[i], cur_sight):
                    i = i + 1
                else:
                    self.insights.insert(i, cur_sight)
                    break
            if i == len(self.insights):
                self.insights.insert(i, cur_sight)

        else:
            self.insights.insert(0, [name, score])

    def get(self) -> str:
        self.idx += 1
        return self.insights[self.idx][0]

    def cmp(self, sight1, sight2):
        name1, score1 = sight1
        name2, score2 = sight2
        if score1 > score2:
            return True
        elif score1 == score2 and name1 < name2:
            return True
        else:
            return False

# ["SORTracker", "add", "add", "get", "add", "get", "add", "get", "add", "get", "add", "get", "get"]
# [[], ["bradford", 2], ["branford", 3], [], ["alps", 2], [], ["orland", 2], [], ["orlando", 3], [], ["alpine", 2], [], []]
# [null, null, null, "branford", null, "alps", null, "bradford", null, "bradford", null, "bradford", "orland"]


if __name__ == "__main__":
    tracker = SORTracker()
    tracker.add("bradford", 2)
    tracker.add("branford", 3)
    print(tracker.get())
    tracker.add("alps", 2)
    print(tracker.get())
    # print(tracker.insights)








    # sol = Solution()
    # # bombs = [[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]
    # # bombs = [[54,95,4],[99,46,3],[29,21,3],[96,72,8],[49,43,3],[11,20,3],[2,57,1],[69,51,7],[97,1,10],[85,45,2],[38,47,1],[83,75,3],[65,59,3],[33,4,1],[32,10,2],[20,97,8],[35,37,3]]
    # # bombs = [[2, 1, 3], [6, 1, 4]]
    # # bombs = [[7, 26, 7], [7, 18, 4], [3, 10, 7], [17, 50, 1], [3, 25, 10], [85, 23, 8], [80, 50, 1], [58, 74, 1], [38, 39, 7],
    # #  [50, 51, 8], [31, 99, 3], [53, 6, 5], [59, 27, 10], [87, 78, 9], [68, 58, 3]] # 3
    # # bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
    # bombs = [[855, 82, 158], [17, 719, 430], [90, 756, 164], [376, 17, 340], [691, 636, 152], [565, 776, 5], [464, 154, 271],
    #  [53, 361, 162], [278, 609, 82], [202, 927, 219], [542, 865, 377], [330, 402, 270], [720, 199, 10], [986, 697, 443],
    #  [471, 296, 69], [393, 81, 404], [127, 405, 177]]
    # print(sol.maximumDetonation(bombs))



    # security = [5, 3, 3, 3, 5, 6, 2]
    # time = 9
    # print(sol.goodDaysToRobBank(security, time))


    # nums = [3,3, 4, 3, 3]
    # k = 4
    # print(sol.maxSubsequence(nums,k))