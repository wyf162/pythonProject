# _*_ coding: utf-8 _*_
# @Time : 2023/01/07 4:29 PM 
# @Author : yefe
# @File : 60_get_permutation

from math import factorial

facts = [factorial(i) for i in range(10)]


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        level = 1
        nums = [i+1 for i in range(n)]
        ans = ""
        while level <= n:
            idx = k // facts[n-level]
            k = k % facts[n-level]
            ans += str(nums[idx])
            nums.remove(nums[idx])
            print(k)
            print(nums)
            level += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    n = 3
    k = 3
    ret = sol.getPermutation(n, k)
    print(ret)
