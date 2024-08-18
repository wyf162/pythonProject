# -*- coding : utf-8 -*-
# @Time: 2024/8/18 10:28
# @Author: yefei.wang
# @File: B.py

from typing import List


class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        n = len(energyDrinkA)
        dpA = [0] * (n + 1)
        dpB = [0] * (n + 1)
        dpA[0] = energyDrinkA[0]
        dpB[0] = energyDrinkB[0]
        for i in range(1, n):
            dpA[i] = max(dpA[i - 1], dpB[i - 2]) + energyDrinkA[i]
            dpB[i] = max(dpB[i - 1], dpA[i - 2]) + energyDrinkB[i]
        ret = max(dpA[n - 1], dpB[n - 1])
        return ret


if __name__ == '__main__':
    sol = Solution()
    # energyDrinkA = [1, 3, 1]
    # energyDrinkB = [3, 1, 1]
    energyDrinkA = [4, 1, 1]
    energyDrinkB = [1, 1, 3]
    ret = sol.maxEnergyBoost(energyDrinkA, energyDrinkB)
    print(ret)
