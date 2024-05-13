# _*_ coding: utf-8 _*_
# @Time : 2022/05/02 2:08 PM 
# @Author : yefe
# @File : 17006_number_of_2s_in_range
import math


class Solution:
    def numberOf2sInRange(self, n: int) -> int:
        if n == 0:
            return 0
        digit = int(math.log10(n)) + 1
        # 初始化数组dp,counters
        # dp[i] 表示n的1~i位组成的数字所包含2的个数
        # counters[i] = numberOf2sInRange(10**(i-1)-1)
        dp = [0] * (digit + 1)
        counters = [0] * (digit + 1)
        dp[1] = 1 if n % 10 >= 2 else 0
        counters[1] = 1
        for i in range(2, digit + 1):
            k = int(n / math.pow(10, i - 1)) % 10
            dp[i] = k * counters[i - 1] + dp[i - 1]
            if k > 2:
                dp[i] += int(math.pow(10, i - 1))
            elif k == 2:
                dp[i] += n % int(math.pow(10, i - 1)) + 1
            counters[i] = 10 * counters[i - 1] + int(math.pow(10, i - 1))
        return dp[digit]


if __name__ == '__main__':
    sol = Solution()
    n = 25
    res = sol.numberOf2sInRange(n)
    print(n)
