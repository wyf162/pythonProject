import sys
import typing


class FenwickTree:
    '''Reference: https://en.wikipedia.org/wiki/Fenwick_tree'''

    def __init__(self, n: int = 0) -> None:
        self._n = n
        self.data = [0] * n

    def add(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p

    def sum(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n

        return self._sum(right) - self._sum(left)

    def _sum(self, r: int) -> typing.Any:
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r

        return s


sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())

tcn = I()
for _tcn_ in range(tcn):
    n, m = MI()
    ones = [0] * m
    tot = [0] * m
    segments = []
    for i in range(m):
        l, r = GMI()
        segments.append([l, r])
        tot[i] = r - l + 1
    q = I()
    queries = [I() - 1 for _ in range(q)]


    def check(mid):
        fwt = FenwickTree(n)
        for i in range(mid):
            fwt.add(queries[i], 1)

        for left, right in segments:
            s = fwt.sum(left, right + 1)
            if s * 2 > right - left + 1:
                return True
        return False


    ans = -1
    L, R = 1, q
    while L <= R:
        mid = (L + R) // 2
        if check(mid):
            ans = mid
            R = mid - 1
        else:
            L = mid + 1

    print(ans)
