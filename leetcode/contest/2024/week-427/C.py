from typing import List


class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ret = -10**18
        pre_sum = [0] * (n + 1)
        for i, num in enumerate(nums):
            pre_sum[i + 1] = pre_sum[i] + num

        groups = [[pre_sum[i]] for i in range(k)]

        for i in range(k, n + 1, 1):
            idx = i % k
            groups[idx].append(pre_sum[i])
        print(groups)

        for i in range(k):
            group = groups[i]
            mx_dp = [0] * len(group) + [-10**18]
            for i in range(len(group)-1, -1, -1):
                mx_dp[i] = max(mx_dp[i+1], group[i])

            for i in range(len(group)):
                ret = max(ret, mx_dp[i+1] - group[i])
        return ret


if __name__ == '__main__':
    sol = Solution()
    # nums = [1, 2]
    nums = [-1, -2, -3, -4, -5]
    k = 4
    ret = sol.maxSubarraySum(nums, k)
    print(ret)
