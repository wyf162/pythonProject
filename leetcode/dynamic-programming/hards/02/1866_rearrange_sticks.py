# _*_ coding: utf-8 _*_
# @Time : 2022/08/30 9:56 PM 
# @Author : yefe
# @File : 1866_rearrange_sticks


class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        MOD = 10**9+7

        f = [1] + [0]*k

        for i in range(1, n+1):
            g = [0] * (k+1)
            for j in range(1, k+1):
                g[j] = f[j]*(i-1) + f[j-1]
                g[j] %= MOD
            f = g
        return f[k]


if __name__ == '__main__':
    sol = Solution()
    ret = sol.rearrangeSticks(4, 1)
    print(ret)
