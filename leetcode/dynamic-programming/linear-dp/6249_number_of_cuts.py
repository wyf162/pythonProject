# _*_ coding: utf-8 _*_
# @Time : 2022/11/27 1:57 PM 
# @Author : yefe
# @File : 6249_number_of_cuts
class Solution:
    def numberOfCuts(self, n: int) -> int:
        f = [i for i in range(n + 1)]
        f[1] = 0
        f[2] = 1
        for i in range(3, n + 1):
            for j in range(2, i):
                if i % j == 0:
                    f[i] = min(f[j]*(i//j), f[i])
        print(f)
        return f[n]


if __name__ == '__main__':
    sol = Solution()
    n = 100
    ret = sol.numberOfCuts(n)
    print(ret)
