# _*_ coding: utf-8 _*_
# @Time : 2022/11/05 9:12 PM 
# @Author : yefe
# @File : 1502_min_integer2


class BIT:
    def __init__(self, n: int):
        self.n = n
        self.tree = [0] * (n + 1)

    @staticmethod
    def lowbit(x: int) -> int:
        return x & (-x)

    def update(self, x: int):
        while x <= self.n:
            self.tree[x] += 1
            x += BIT.lowbit(x)

    def query(self, x: int) -> int:
        ans = 0
        while x > 0:
            ans += self.tree[x]
            x -= BIT.lowbit(x)
        return ans

    def queryRange(self, x: int, y: int) -> int:
        return self.query(y) - self.query(x - 1)


class Solution:
    def minInteger(self, num: str, k: int) -> str:
        n = len(num)
        pos = [list() for _ in range(10)]
        for i in range(n - 1, -1, -1):
            pos[ord(num[i]) - ord('0')].append(i + 1)

        ans = ""
        bit = BIT(n)
        for i in range(1, n + 1):
            for j in range(10):
                if pos[j]:
                    behind = bit.queryRange(pos[j][-1] + 1, n)
                    dist = pos[j][-1] + behind - i
                    if dist <= k:
                        bit.update(pos[j][-1])
                        pos[j].pop()
                        ans += str(j)
                        k -= dist
                        break

        return ans
