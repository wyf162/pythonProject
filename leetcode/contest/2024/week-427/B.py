from typing import List
import itertools


class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        n = len(points)
        ret = -1

        for idxs in itertools.combinations(list(range(n)), 4):
            select_points = [points[idx] for idx in idxs]
            select_points.sort()
            p1, p2, p3, p4 = select_points
            if p1[0] == p2[0] and p1[1] == p3[1] and p2[1] == p4[1] and p3[0] == p4[0]:
                left = p1[0]
                right = p3[0]
                down = p1[1]
                up = p2[1]
                for i in range(n):
                    if i in idxs:
                        continue
                    if left <= points[i][0] <= right and down <= points[i][1] <= up:
                        break

                else:
                    w = p3[0] - p1[0]
                    h = p2[1] - p1[1]
                    area = w * h
                    ret = max(area, ret)
        return ret


if __name__ == '__main__':
    sol = Solution()
    points = [[1, 1], [1, 3], [3, 1], [3, 3]]
    points = points = [[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]
    ret = sol.maxRectangleArea(points)
    print(ret)
