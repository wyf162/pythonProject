import bisect
import collections
import heapq
import math
import platform
import sys
from bisect import bisect_left
from typing import List
from sortedcontainers import SortedList


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        ret = set(nums[0])
        for i in range(1, len(nums)):
            ret = ret & set(nums[i])
        ret = list(ret)
        ret.sort()
        return ret

    def countLatticePoints(self, circles: List[List[int]]) -> int:
        visited = set()
        for circle in circles:
            x, y, r = circle
            left, right = math.floor(x - r), math.floor(x + r)
            down, up = math.floor(y - r), math.ceil(y + r)
            for xi in range(left, right + 1, 1):
                for yi in range(down, up + 1, 1):
                    if (xi - x) * (xi - x) + (yi - y) * (yi - y) <= r * r:
                        visited.add((xi, yi))
        return len(visited)

    def countRectangles2(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        rets = list()
        x_list = [(r[0], i) for i, r in enumerate(rectangles)]
        x_list.sort()
        x_len = [x[0] for x in x_list]
        x_idx = [x[1] for x in x_list]
        
        y_list = [(r[1], i) for i, r in enumerate(rectangles)]
        y_list.sort()
        y_len = [y[0] for y in y_list]
        y_idx = [y[1] for y in y_list]

        for point in points:
            x, y = point
            idx_x = bisect.bisect_left(x_len, x)
            idx_y = bisect.bisect_left(y_len, y)
            sx = x_idx[idx_x:]
            sy = y_idx[idx_y:]
            ss = set(sx) & set(sy)
            ret = len(ss)
            rets.append(ret)
        return rets

    def countRectangles(self, rectangles, points):
        rectangles.sort(key=lambda r: -r[1])
        n = len(points)
        ans = [0] * n
        i, xs = 0, SortedList()
        for (x, y), id in sorted(zip(points, range(n)), key=lambda x: -x[0][1]):
            while i < len(rectangles) and rectangles[i][1] >= y:
                xs.add(rectangles[i][0])
                i += 1
            ans[id] = i - xs.bisect_left(x)
        return ans

    def countRectangles3(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        rectangles.sort(key=lambda r: -r[1])
        n = len(points)
        ans = [0] * n
        i, xs = 0, []
        for (x, y), idx in sorted(zip(points, range(n)), key=lambda x: -x[0][1]):
            start = i
            while i < len(rectangles) and rectangles[i][1] >= y:
                xs.append(rectangles[i][0])
                i += 1
            if start < i:
                xs.sort()  # 只有在 xs 插入了新元素时才排序
            ans[idx] = i - bisect_left(xs, x)
        return ans

    def fullBloomFlowers2(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        to_ret = [None]*len(persons)
        persons = sorted([[t, i] for i, t in enumerate(persons)])
        flowers.sort()
        heap = list()
        pf = 0
        for t, it in persons:
            while pf<len(flowers) and flowers[pf][0] <= t:
                heapq.heappush(heap, flowers[pf][1])
                pf += 1
            while len(heap) > 0 and heap[0] < t:
                heapq.heappop(heap)
            to_ret[it] = len(heap)
        return to_ret

    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        diff = collections.defaultdict(int)
        for start, end in flowers:
            diff[start] += 1
            diff[end+1] -= 1
        times = sorted(diff.keys())

        n = len(persons)
        ans = [0] * n
        i = s = 0
        for p, idx in sorted(zip(persons, range(n))):
            while i < len(times) and times[i]<=p:
                s += diff[times[i]]
                i += 1
            ans[idx] = s
        return ans


if __name__ == '__main__':
    sol = Solution()
    flowers = [[1, 6], [3, 7], [9, 12], [4, 13]]
    persons = [2, 3, 7, 11]
    ret = sol.fullBloomFlowers(flowers, persons)
    print(ret)

    # rectangles = [[1, 2], [2, 3], [2, 5]]
    # points = [[2, 1], [1, 4]]
    # rectangles = [[1, 1], [2, 2], [3, 3]]
    # points = [[1, 1], [1, 3], [1, 1]]
    #
    # ret = sol.countRectangles(rectangles, points)
    # print(ret)

    # circles = [[2, 2, 2], [3, 4, 1]]
    # ret = sol.countLatticePoints(circles)
    # print(ret)

    # nums = [[1, 2, 3], [4, 5, 6]]
    # # nums = [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]
    # ret = sol.intersection(nums)
    # print(ret)

    # print(sys.version)
    # print(platform.version())
