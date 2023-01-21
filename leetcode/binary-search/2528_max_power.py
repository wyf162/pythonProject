# _*_ coding: utf-8 _*_
# @Time : 2023/01/08 3:45 PM 
# @Author : yefe
# @File : 2528_max_power

from itertools import accumulate
from typing import List


class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        sum = list(accumulate(stations, initial=0))  # 前缀和

        def check(min_power: int) -> bool:
            diff = [0] * (n + 1)  # 差分数组
            sum_d = need = 0
            for i in range(n):
                sum_d += diff[i]  # 累加差分值
                power = sum[min(i + r + 1, n)] - sum[max(i - r, 0)]
                m = min_power - power - sum_d
                if m > 0:  # 需要 m 个供电站
                    need += m
                    if need > k: return False  # 提前退出这样快一些
                    sum_d += m  # 差分更新
                    diff[min(i + r * 2 + 1, n)] -= m  # 差分更新
            return True

        left, right = -1, sum[-1] + k + 1  # 开区间写法
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid): left = mid
            else: right = mid
        return left


if __name__ == '__main__':
    sol = Solution()
    # stations = [1, 2, 4, 5, 0]
    # r = 1
    # k = 2
    stations = [4, 4, 4, 4]
    r = 0
    k = 3
    ret = sol.maxPower(stations, r, k)
    print(ret)
