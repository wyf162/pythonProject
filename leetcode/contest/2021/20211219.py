# -*- coding : utf-8 -*-
# @Time: 2021/12/19 10:32
# @Author: yefei.wang
# @File: 20211219.py
from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.is_palindrome(word):
                return word
        return ""

    def is_palindrome(self, s1):
        if len(s1)==1:
            return True
        i = len(s1) >> 1
        pre = list(s1[0:i])
        post = list(s1[-i:])
        post.reverse()
        return pre == post

    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ""
        i,j = 0,0
        while i<len(s):
            if i==spaces[j]:
                ans = ans + " " + s[i]
                j = j+1
                if j==len(spaces):
                    i = i + 1
                    break
            else:
                ans = ans + s[i]
            i = i+1
        ans = ans+s[i:]
        print(ans)
        return ans

    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = 0
        i = 0
        n = len(prices)
        while i < n:
            tail = prices[i]
            cnt = 1
            while i + 1 < n and prices[i + 1] == tail - 1:
                cnt += 1
                tail = prices[i + 1]
                i = i + 1
            ans += self.compute(cnt)
            i = i + 1
        return ans

    def compute(self, n):
        return int(n * (n + 1) / 2)

    def kIncreasing(self, arr: List[int], k: int) -> int:
        ans = 0
        for i in range(0,k):
            selected_arr = arr[i:len(arr):k]
            t = self.lengthOfLIS(selected_arr)
            print("ttt:", t)
            ans = ans + len(selected_arr) - t
        return ans
        # left, right = 0, len(arr)
        # while left<right:
        #     mid = (left+right)>>1
        #     if self.is_valid(arr, k, mid):
        #         right = mid
        #     else:
        #         left = mid+1
        # return left

    def is_valid(self, arr, k, n):
        ans = 0
        for i in range(0,k):
            selected_arr = arr[i:len(arr):k]
            t = self.lengthOfLIS(selected_arr)
            ans += len(selected_arr)-t
        return ans<=n

    def increased_stack(self, nums):
        ans = 0
        stk = list()
        i, n = 0, len(nums)
        while i<n:
            if not stk:
                stk.append(nums[i])
            else:
                if nums[i]>=stk[-1]:
                    stk.append(nums[i])
                else:
                    while stk and stk[-1]>nums[i]:
                        stk.pop()
                    stk.append(nums[i])
            ans = max(ans,len(stk))
            i = i+1
        return ans

    def lengthOfLIS(self, nums: List[int]) -> int:
        d = []
        for n in nums:
            if not d or n >= d[-1]:
                d.append(n)
            else:
                l, r = 0, len(d) - 1
                loc = r
                while l <= r:
                    mid = (l + r) // 2
                    if d[mid] > n:
                        loc = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                d[loc] = n
        return len(d)


if __name__ == "__main__":
    sol = Solution()
    # arr = [5, 4, 3, 2, 1]
    # k = 1
    # arr = [4, 1, 5, 2, 6, 2]
    # k = 2
    # arr = [4, 1, 5, 2, 6, 2]
    # k = 3
    # arr = [12,6,12,6,14,2,13,17,3,8,11,7,4,11,18,8,8,3]
    # k = 1
    arr = [2,2,2,2,2,1,1,4,4,3,3,3,3,3]
    k = 1
    sol.kIncreasing(arr, k)
    print(sol.kIncreasing(arr, k))

    print(sol.lengthOfLIS(arr))

    # prices = [3, 2, 1, 0, 5, 4]
    # prices = [8, 6, 7, 7]
    # print(sol.getDescentPeriods(prices))

    # s = "LeetcodeHelpsMeLearn"
    # spaces = [8, 13, 15]
    # sol.addSpaces(s,spaces)
    # s = "spacing"
    # spaces = [0, 1, 2, 3, 4, 5, 6]
    # sol.addSpaces(s, spaces)
    # words = ["notapalindrome",'abda',"racdecar"]
    # print(sol.firstPalindrome(words))