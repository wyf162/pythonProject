# _*_ coding: utf-8 _*_
# @Time : 2021/11/13 下午10:29 
# @Author : wangyefei
# @File : 20211113.py
from typing import List


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items = sorted(items, key=lambda x: (x[0], -x[1]))
        dp = []
        tmp = 0
        for price, beauty in items:
            if not dp:
                tmp = max(tmp, beauty)
                dp.append([price, tmp])
            else:
                if price == dp[-1][0]:
                    continue
                else:
                    tmp = max(tmp, beauty)
                    dp.append([price, max(beauty, tmp)])
        print(dp)
        ans = []
        for q in queries:
            ans.append(self.query(dp, q))
        return ans

    def query(self, dp, target):
        left, right = 0, len(dp)
        while left < right:
            mid = left + (right-left>>1)
            if dp[mid][0] > target:
                right = mid - 1
            else:
                left = mid + 1
        if left==len(dp):
            return dp[left-1][1]
        elif left==0 and dp[left][0]>target:
            return 0
        elif dp[left][0]>target:
            return dp[left-1][0]
        else:
            return dp[left][0]

    def search(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = left + (right - left>>1)
            print(left, right ,mid)
            if nums[mid]>target:
                right = mid-1
            else:
                left = mid+1
        if left==len(nums) or nums[left]>target:
            return left-1
        else:
            return left


class Robot:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.direction = 'East'
        self.location = [0, 0, 'East']
        self.idx = 0
        self.locations = []
        for i in range(1, self.width):
            self.locations.append([i, 0, 'East'])
        for j in range(1, self.height):
            self.locations.append([self.width - 1, j, 'North'])
        for i in range(self.width - 2, -1, -1):
            self.locations.append([i, self.height - 1, 'West'])
        for j in range(self.height - 2, 0, -1):
            self.locations.append([0, j, 'South'])
        self.locations.insert(0, [0, 0, 'South'])

    def move(self, num: int) -> None:
        self.idx = (self.idx + num) % (self.width * 2 + self.height * 2 - 4)
        self.location = self.locations[self.idx]

    def getPos(self) -> List[int]:
        return self.location[0:2]

    def getDir(self) -> str:
        return self.location[2]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.move(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()


if __name__ == "__main__":
    robot = Robot(6, 3)
    print(robot.locations)
    robot.move(6)
    print(robot.getPos())

    # items = [[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]]
    # queries = [0, 2, 3, 4, 5, 6]
    # sol = Solution()
    # ans = sol.maximumBeauty(items, queries)
    # # nums = [1, 3, 5]
    # # target = 4
    # # ans = sol.search(nums, target)
    # print(ans)
