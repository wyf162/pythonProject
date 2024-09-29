from typing import List
from itertools import permutations


class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        ans = 0
        for perm in permutations(nums):
            s = ''
            for x in perm:
                s += bin(x)[2:]
            ans = max(ans, int(s, 2))
        return ans


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3]
    ret = sol.maxGoodNumber(nums)
    print(ret)
