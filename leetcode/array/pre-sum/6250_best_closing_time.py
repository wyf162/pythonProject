# _*_ coding: utf-8 _*_
# @Time : 2022/11/27 2:23 PM 
# @Author : yefe
# @File : 6250_best_closing_time

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        pres = [0]
        for i in range(n):
            if customers[i] == 'Y':
                pres.append(pres[-1] + 1)
            else:
                pres.append(pres[-1] + 0)

        best, cost = n, n - pres[-1]

        for i in range(n):
            cur_cost = i - pres[i] + pres[-1] - pres[i]
            if cur_cost < cost or (cur_cost == cost and i < best):
                cost = cur_cost
                best = i
        return best


if __name__ == '__main__':
    sol = Solution()
    customers = "YYNY"
    ret = sol.bestClosingTime(customers)
    print(ret)
