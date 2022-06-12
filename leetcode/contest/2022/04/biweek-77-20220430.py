# _*_ coding: utf-8 _*_
# @Time : 2022/04/30 10:28 PM 
# @Author : yefe
# @File : biweek-77-20220430
import bisect
from typing import List


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        pre = [0]
        for num in nums:
            pre.append(pre[-1] + num)
        ret = pre[-1] // n
        idx = n - 1
        for i in range(n - 2, -1, -1):
            a = pre[i + 1] // (i + 1)
            b = (pre[-1] - pre[i + 1]) // (n - i - 1)
            if ret >= abs(a - b):
                ret = abs(a - b)
                idx = i
        return idx

    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        unvisited = [[1 for j in range(n)] for i in range(m)]
        cnt = 0
        for x, y in guards:
            unvisited[x][y] = 2
        for x, y in walls:
            unvisited[x][y] = 2
        for guard in guards:
            x, y = guard
            x -= 1
            while x >= 0:
                if unvisited[x][y] < 2:
                    cnt += unvisited[x][y]
                    unvisited[x][y] = 0
                    x -= 1
                else:
                    break
            x, y = guard
            x += 1
            while x < m:
                if unvisited[x][y] < 2:
                    cnt += unvisited[x][y]
                    unvisited[x][y] = 0
                    x += 1
                else:
                    break
            x, y = guard
            y -= 1
            while y >= 0:
                if unvisited[x][y] < 2:
                    cnt += unvisited[x][y]
                    unvisited[x][y] = 0
                    y -= 1
                else:
                    break
            x, y = guard
            y += 1
            while y < n:
                if unvisited[x][y] < 2:
                    cnt += unvisited[x][y]
                    unvisited[x][y] = 0
                    y += 1
                else:
                    break

        # print(cnt)
        return m * n - cnt - len(walls) - len(guards)

    def maximumMinutes(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def check(t: int) -> bool:
            f = [(i, j) for i, row in enumerate(grid) for j, v in enumerate(row) if v == 1]
            fire = set(f)

            def spread_fire():
                nonlocal f
                tmp = f
                f = []
                for i, j in tmp:
                    for x, y in ((i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)):
                        if 0 <= x < m and 0 <= y < n and grid[x][y] != 2 and (x, y) not in fire:
                            fire.add((x, y))
                            f.append((x, y))

            while t and f:
                spread_fire()
                t -= 1
            if (0, 0) in fire:
                return True

            q = [(0, 0)]
            vis = set(q)
            while q:
                tmp = q
                q = []
                for i, j in tmp:
                    if (i, j) not in fire:
                        for x, y in ((i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)):
                            if 0 <= x < m and 0 <= y < n and grid[x][y] != 2 and (x, y) not in fire and (x, y) not in vis:
                                if x == m - 1 and y == n - 1:
                                    return False
                                vis.add((x, y))
                                q.append((x, y))
                spread_fire()
            return True

        # ans = bisect.bisect_left(range(m*n+1), True, key=check)-1
        l, r = 0, m * n + 1
        while l < r:
            mid = (l + r) >> 1
            print(mid, l, r)
            if not check(mid):
                l = mid + 1
            else:
                r = mid
        ans = l-1
        print(ans)
        return ans if ans < m * n else int(1e9)


if __name__ == '__main__':
    sol = Solution()
    # grid = [[0, 2, 0, 0, 0, 0, 0], [0, 0, 0, 2, 2, 1, 0], [0, 2, 0, 0, 1, 2, 0], [0, 0, 2, 2, 2, 0, 2],
    #         [0, 0, 0, 0, 0, 0, 0]]
    grid = [[0, 0, 0, 0], [0, 1, 2, 0], [0, 2, 0, 0]]
    ret = sol.maximumMinutes(grid)
    print(ret)
    # m = 4
    # n = 6
    # guards = [[0, 0], [1, 1], [2, 3]]
    # walls = [[0, 1], [2, 2], [1, 4]]
    # m = 3
    # n = 3
    # guards = [[1, 1]]
    # walls = [[0, 1], [1, 0], [2, 1], [1, 2]]
    # m = 1
    # n = 5
    # guards = [[0, 0]]
    # walls = [[0,1]]
    # ret = sol.countUnguarded(m, n, guards, walls)
    # print(ret)
    # nums = [2, 2]
    # ret = sol.minimumAverageDifference(nums)
    # print(ret)
