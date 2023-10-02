# _*_ coding: utf-8 _*_
# @Time : 2022/12/05 8:59 PM 
# @Author : yefe
# @File : 1687_box_delivering

from typing import List
from math import inf
from collections import deque


class Solution2:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:

        def dfs(i):
            if i <= 0:
                return 0
            else:
                ret = inf
                c, w = 0, 0
                v = 0
                port = -1
                for j in range(i - 1, -1, -1):
                    c += 1
                    w += boxes[j][1]
                    if c > maxBoxes or w > maxWeight:
                        break
                    if port < 0:
                        v += 1
                    elif port == boxes[j][0]:
                        v += 0
                    else:
                        v += 1
                    port = boxes[j][0]
                    ret = min(ret, dfs(j) + v + 1)
                return ret

        return dfs(len(boxes))


class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        def getArray() -> List[int]:
            return [0] * (n + 1)

        n = len(boxes)
        p, w, neg, W = getArray(), getArray(), getArray(), getArray()

        for i in range(1, n + 1):
            p[i], w[i] = boxes[i - 1]
            if i > 1:
                neg[i] = neg[i - 1] + (p[i - 1] != p[i])
            W[i] = W[i - 1] + w[i]

        opt = deque([0])
        f, g = getArray(), getArray()

        for i in range(1, n + 1):
            while i - opt[0] > maxBoxes or W[i] - W[opt[0]] > maxWeight:
                opt.popleft()

            f[i] = g[opt[0]] + neg[i] + 2

            if i != n:
                g[i] = f[i] - neg[i + 1]
                while opt and g[i] <= g[opt[-1]]:
                    opt.pop()
                opt.append(i)

        return f[n]


if __name__ == '__main__':
    sol = Solution()
    boxes = [[1, 2], [3, 3], [3, 1], [3, 1], [2, 4]]
    portsCount = 3
    maxBoxes = 3
    maxWeight = 6
    ret = sol.boxDelivering(boxes, portsCount, maxBoxes, maxWeight)
    print(ret)
