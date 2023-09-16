# _*_ coding: utf-8 _*_
# @Time : 2022/06/04 3:03 PM 
# @Author : yefe
# @File : 1515_get_min_dist_sum
from math import sqrt
from random import random
from typing import List


class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        eps = 1e-7
        alpha = 1.0
        decay = 1e-3

        n = len(positions)
        # 调整批大小
        batchSize = n

        x = sum(pos[0] for pos in positions) / n
        y = sum(pos[1] for pos in positions) / n

        # 计算服务中心 (xc, yc) 到客户的欧几里得距离之和
        getDist = lambda xc, yc: sum(((x - xc) ** 2 + (y - yc) ** 2) ** 0.5 for x, y in positions)

        while True:
            # 将数据随机打乱
            random.shuffle(positions)
            xPrev, yPrev = x, y

            for i in range(0, n, batchSize):
                j = min(i + batchSize, n)
                dx, dy = 0.0, 0.0

                # 计算导数，注意处理分母为零的情况
                for k in range(i, j):
                    pos = positions[k]
                    dx += (x - pos[0]) / (sqrt((x - pos[0]) * (x - pos[0]) + (y - pos[1]) * (y - pos[1])) + eps)
                    dy += (y - pos[1]) / (sqrt((x - pos[0]) * (x - pos[0]) + (y - pos[1]) * (y - pos[1])) + eps)

                x -= alpha * dx
                y -= alpha * dy

                # 每一轮迭代后，将学习率进行衰减
                alpha *= (1.0 - decay)

            # 判断是否结束迭代
            if ((x - xPrev) ** 2 + (y - yPrev) ** 2) ** 0.5 < eps:
                break

        return getDist(x, y)

