# _*_ coding: utf-8 _*_
# @Time : 2022/08/31 11:34 PM 
# @Author : yefe
# @File : 1553_min_days


class Solution:
    def minDays(self, n: int) -> int:
        f = [0] * (n + 1)
        f[1] = 1
        for i in range(2, n + 1):
            f[i] = f[i - 1] + 1
            if i % 2 == 0:
                f[i] = min(f[i], f[i // 2] + 1)
            if i % 3 == 0:
                f[i] = min(f[i], f[i // 3] + 1)
        return f[n]


if __name__ == '__main__':
    sol = Solution()
    n = 56
    ret = sol.minDays(n)
    print(ret)
