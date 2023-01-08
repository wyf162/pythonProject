# _*_ coding: utf-8 _*_
# @Time : 2023/01/02 8:18 PM 
# @Author : yefe
# @File : 1801_get_number_of_backlog_orders

import heapq
from typing import List


class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buy_pq = []
        sell_pq = []

        for order in orders:
            price, amount, order_type = order
            if order_type == 0:
                while amount and sell_pq and sell_pq[0][0] <= price:
                    if amount < sell_pq[0][1]:
                        s_price, s_amount = heapq.heappop(sell_pq)
                        heapq.heappush(sell_pq, [s_price, s_amount - amount])
                        amount = 0
                    else:
                        s_price, s_amount = heapq.heappop(sell_pq)
                        amount -= s_amount
                if amount:
                    heapq.heappush(buy_pq, [-price, amount])

            if order_type == 1:
                while amount and buy_pq and buy_pq[0][0] <= price:
                    if amount < buy_pq[0][1]:
                        b_price, b_amount = heapq.heappop(buy_pq)
                        heapq.heappush(buy_pq, [b_price, b_amount - amount])
                        amount = 0
                    else:
                        b_price, b_amount = heapq.heappop(buy_pq)
                        amount -= b_amount
                if amount:
                    heapq.heappush(sell_pq, [price, amount])
        ans = 0
        for price, amount in buy_pq:
            ans += amount
        for price, amount in sell_pq:
            ans += amount

        ans %= 1000000007
        return ans


if __name__ == '__main__':
    sol = Solution()
    orders = [[10, 5, 0], [15, 2, 1], [25, 1, 1], [30, 4, 0]]
    ret = sol.getNumberOfBacklogOrders(orders)
    print(ret)

