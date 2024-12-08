from typing import List


class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        for i, num in enumerate(nums):
            idx = (i + num) % n
            result[i] = nums[idx]
        return result


if __name__ == "__main__":
    sol = Solution()
    nums = [3, -2, 1, 1]
    nums = [-1, 4, -1]
    ret = sol.constructTransformedArray(nums)
    print(ret)
