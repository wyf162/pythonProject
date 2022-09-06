# _*_ coding: utf-8 _*_
# @Time : 2022/09/06 10:51 PM 
# @Author : yefe
# @File : 907_sum_subarray_mins

from typing import List


class Solution(object):
    def sumSubarrayMins2(self, arr):
        MOD = 10 ** 9 + 7

        stack = []
        ans = dot = 0
        for j, y in enumerate(arr):
            # Add all answers for subarrays [i, j], i <= j
            count = 1
            while stack and stack[-1][0] >= y:
                x, c = stack.pop()
                count += c
                dot -= x * c

            stack.append((y, count))
            dot += y * count
            ans += dot
        return ans % MOD

    def sumSubarrayMins(self, arr):
        MOD = 10 ** 9 + 7
        n = len(arr)

        # left_bound = [-1] * n
        # stk = []
        # for i in range(n - 1, -1, -1):
        #     while stk and arr[stk[-1]] >= arr[i]:
        #         left_bound[stk.pop()] = i
        #     stk.append(i)
        # print(left_bound)
        #
        # right_bound = [n] * n
        # stk = []
        # for i in range(n):
        #     while stk and arr[stk[-1]] > arr[i]:
        #         right_bound[stk.pop()] = i
        #     stk.append(i)
        # print(right_bound)

        # prev smaller
        left_bound = [-1] * n
        stk = []
        for i in range(n):
            while stk and arr[stk[-1]] >= arr[i]:
                stk.pop()
            if stk:
                left_bound[i] = stk[-1]
            stk.append(i)
        print(left_bound)

        # next smaller
        right_bound = [n] * n
        stk = []
        for i in range(n - 1, -1, -1):
            while stk and arr[stk[-1]] > arr[i]:
                stk.pop()
            if stk:
                right_bound[i] = stk[-1]
            stk.append(i)
        print(right_bound)
        ans = 0
        for i in range(n):
            a, b = left_bound[i], right_bound[i]
            ans += (i - a) * (b - i) * arr[i]
            ans %= MOD
        ans %= MOD
        return ans


if __name__ == '__main__':
    sol = Solution()
    arr = [3, 1, 2, 4]
    ret = sol.sumSubarrayMins(arr)
    print(ret)
