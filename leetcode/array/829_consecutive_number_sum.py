# _*_ coding: utf-8 _*_
# @Time : 2022/06/03 9:43 AM 
# @Author : yefe
# @File : 829_consecutive_number_sum

class Solution:
    def consecutiveNumbersSum2(self, n: int) -> int:

        def is_consecutive(n, k):
            if k % 2:
                return n % k == 0
            return n % k and 2 * n % k == 0

        ans = 0
        k = 1
        while k * (k + 1) <= n*2:
            if is_consecutive(n, k):
                print(k)
                ans += 1
            k += 1
        return ans

    def consecutiveNumbersSum(self, n: int) -> int:

        def is_consecutive(n, k):
            s = (1 + k) * k // 2
            return (n - s) % k == 0

        ans = 0
        k = 1
        while k * (k + 1) <= n*2:
            if is_consecutive(n, k):
                print(k)
                ans += 1
            k += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    n = 5
    print(sol.consecutiveNumbersSum2(n))
    print(sol.consecutiveNumbersSum(n))
