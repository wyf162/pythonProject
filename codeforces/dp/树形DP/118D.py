import sys
from collections import Counter

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))
mod = 10 ** 9 + 7

n1, n2, k1, k2 = MI()
n = n1 + n2
k = k1 + k2
# (x, y, 0 or 1, c)
mod = 10 ** 8
dp = Counter()

dp[(0, 0, 0, 0)] = 1
# dp[(0, 0, 1, 0)] = 1

for i in range(1, n1 + 1):
    for j in range(n2 + 1):
        # footman + footman
        for x in range(k1):
            dp[(i, j, 0, x + 1)] += dp[(i - 1, j, 0, x)]
            dp[(i, j, 0, x + 1)] %= mod
        # footman + horseman
        for x in range(k1 + 1):
            dp[(i, j, 1, 1)] += dp[(i, j - 1, 0, x)]
            dp[(i, j, 1, 1)] %= mod

        # horseman + horseman
        for x in range(0, k2):
            dp[(i, j, 1, x + 1)] += dp[(i, j - 1, 1, x)]
            dp[(i, j, 1, x + 1)] %= mod
        # horseman + footman
        for x in range(0, k2 + 1):
            dp[(i, j, 0, 1)] += dp[(i - 1, j, 1, x)]
            dp[(i, j, 0, 1)] %= mod

ans = 0
for k, v in dp.items():
    if k[0] == n1 and k[1] == n2:
        ans += dp[k]
print(ans)
