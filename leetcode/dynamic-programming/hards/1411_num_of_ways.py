# _*_ coding: utf-8 _*_
# @Time : 2022/08/22 11:31 PM 
# @Author : yefe
# @File : 1411_num_of_ways


class Solution:

    def numOfWays(self, n: int) -> int:
        mod = 10 ** 9 + 7

        types = list()
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    if i != j and j != k:
                        types.append(i * 9 + j * 3 + k)

        type_cnt = len(types)
        related = [[0] * type_cnt for _ in range(type_cnt)]
        for i, ti in enumerate(types):
            x1, x2, x3 = ti // 9, ti // 3 % 3, ti % 3
            for j, tj in enumerate(types):
                y1, y2, y3 = tj // 9, tj // 3 % 3, tj % 3
                if x1 != y1 and x2 != y2 and x3 != y3:
                    related[i][j] = 1

        f = [[0] * type_cnt for _ in range(n + 1)]
        f[1] = [1] * type_cnt
        for i in range(2, n + 1):
            for j in range(type_cnt):
                for k in range(type_cnt):
                    if related[k][j]:
                        f[i][j] += f[i - 1][k]
                        f[i][j] %= mod

        return sum(f[-1]) % mod


if __name__ == '__main__':
    sol = Solution()
    n = 2
    ret = sol.numOfWays(n)
    print(ret)
