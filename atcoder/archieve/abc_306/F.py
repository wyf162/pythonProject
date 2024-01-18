import sys
from sortedcontainers import SortedList

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

n, m = LI()
mtx = [LI() for _ in range(n)]
ans = 0

sl = SortedList()
for i in range(n):
    r = n - i - 1
    ans += r * (1 + m) * m // 2
    for j in range(m):
        # print(i, j)
        ans += len(sl) - sl.bisect_left(mtx[i][j])
    for j in range(m):
        sl.add(mtx[i][j])
print(ans)
