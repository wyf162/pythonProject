
from typing import List


class Solution:
    def minElement(self, nums: List[int]) -> int:
        return min(sum(int(c) for c in str(num)) for num in nums)