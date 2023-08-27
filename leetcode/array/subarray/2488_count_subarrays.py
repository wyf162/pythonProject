# _*_ coding: utf-8 _*_
# @Time : 2022/11/28 9:58 PM 
# @Author : yefe
# @File : 2488_count_subarrays
from collections import defaultdict
from typing import List


class Solution2:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pres = [0]
        for num in nums:
            if num <= k:
                pres.append(pres[-1] + 1)
            else:
                pres.append(pres[-1] + 0)

        idx = nums.index(k)
        cnt = 0

        for i in range(idx+1):
            for j in range(idx, n):
                if pres[j+1] - pres[i] == (j - i + 1 + 1) // 2:
                    print(i, j)
                    cnt += 1
        return cnt


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        pos = nums.index(k)
        cnt = defaultdict(int)
        cnt[0] = 1  # i=pos 的时候 c 是 0，直接记到 cnt 中，这样下面不是大于就是小于
        c = 0
        for i in range(pos + 1, len(nums)):
            c += 1 if nums[i] > k else -1
            cnt[c] += 1

        ans = cnt[0] + cnt[1]  # i=pos 的时候 c 是 0，直接加到答案中，这样下面不是大于就是小于
        c = 0
        for i in range(pos - 1, -1, -1):
            c += 1 if nums[i] < k else -1
            ans += cnt[c] + cnt[c + 1]
        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [3, 2, 1, 4, 5]
    k = 4
    ret = sol.countSubarrays(nums, k)
    print(ret)
