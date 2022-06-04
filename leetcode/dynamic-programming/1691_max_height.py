# _*_ coding: utf-8 _*_
# @Time : 2022/05/28 5:20 PM 
# @Author : yefe
# @File : 1691_max_height
from typing import List


class Solution2:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        cuboids = [sorted(cuboid) for cuboid in cuboids]
        cuboids.sort(key=lambda x: (x[2], x[1], x[0]))
        n = len(cuboids)
        dp = [0] * n
        for i in range(n):
            dp[i] = cuboids[i][2]
            for j in range(i):
                if cuboids[i][0] >= cuboids[j][0] and cuboids[i][1] >= cuboids[j][1]:
                    dp[i] = max(dp[i], dp[j] + cuboids[i][2])
        return dp[-1]


class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        n = len(cuboids)
        for i in range(n):  # 本题比较简单在于，长、宽、高3个维度，要弱就都弱，不管站着、平躺、侧躺，都弱，就是真的小
            cuboids[i].sort()  # 每个块从小到大排列  大的作为高
        cuboids.sort(key=lambda x: (x[2], x[1], x[0]))  # 按高度，从小到大排列

        dp = [0 for _ in range(n)]
        for R in range(n):  # dp时，后面的依赖前面的，故从前往后遍历
            pre_max = 0  # 跳出前面最大的情况
            for L in range(R):
                if cuboids[L][0] <= cuboids[R][0] and cuboids[L][1] <= cuboids[R][1]:  # 前面的长和宽都小
                    pre_max = max(pre_max, dp[L])
            dp[R] = pre_max + cuboids[R][2]

        return max(dp)


if __name__ == '__main__':
    sol = Solution2()
    # cuboids = [[50, 45, 20], [95, 37, 53], [45, 23, 12]]
    cuboids = [[38,25,45],[76,35,3]]
    ret = sol.maxHeight(cuboids)
    print(ret)
