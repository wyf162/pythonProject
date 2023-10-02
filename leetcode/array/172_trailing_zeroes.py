# _*_ coding: utf-8 _*_
# @Time : 2022/3/25 下午7:48 
# @Author : wangyefei
# @File : 172_trailing_zeroes.py

class Solution:
    def trailingZeroes(self, n: int) -> int:
        cnt_2 = 0
        cnt_5 = 0
        for i in range(1, n + 1):
            k = i
            while k and k % 2 == 0:
                cnt_2 += 1
                k = k // 2
                # print(k)
            k = i
            while k and k % 5 == 0:
                cnt_5 += 1
                k = k // 5
        print(cnt_2, cnt_5)
        return min(cnt_2, cnt_5)


if __name__ == '__main__':
    sol = Solution()
    ret = sol.trailingZeroes(33)
    print(ret)
