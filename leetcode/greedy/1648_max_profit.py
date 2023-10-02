# -*- coding : utf-8 -*-
# @Time: 2022/7/10 16:59
# @Author: yefei.wang
# @File: 1648_max_profit.py
from typing import List

MOD = 10 ** 9 + 7


class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory.sort()
        n = len(inventory)
        s = sum(inventory)
        l = 0
        r = inventory[-1]
        while l < r:
            m = (l + r) >> 1
            cnt = sum([i - m for i in inventory if i > m])
            if cnt == orders:
                l = m
                break
            elif cnt > orders:
                l = m + 1
            else:
                r = m

        residual = orders - sum([i - l for i in inventory if i > l])
        ans = sum([(i + l+1) * (i - l) // 2 for i in inventory if i > l])
        ans += residual * l
        return ans % MOD


if __name__ == '__main__':
    sol = Solution()
    inventory = [2, 5]
    orders = 4  # 14
    # inventory = [3, 5]
    # orders = 6  # 14
    ret = sol.maxProfit(inventory, orders)
    print(ret)
