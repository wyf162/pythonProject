import sys

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

n, m = MI()
grid = [list(input()) for i in range(n)]

for i in range(n):
    for j in range(m):
        if grid[i][j] == '#':
            if i + 1 < n:
                grid[i + 1][j] = '#'
            if i + 1 < n and j + 1 < m:
                grid[i + 1][j + 1] = '#'

for i in range(n):
    print(''.join(grid[i]))

dp = [[[0, 0] for j in range(m)] for i in range(n)]
pre = 1
for j in range(m - 1, -1, -1):
    for i in range(n - 1, -1, -1):
        if grid[i][j] == '#':
            dp[i][j][1] = 1
        else:
            if i + 1 < n and j + 1 < m:
                dp[i][j][1] = dp[i + 1][j][1] * dp[i + 1][j + 1][1]
            elif i + 1 < n:
                dp[i][j][1] = dp[i + 1][j][1]
            else:
                dp[i][j][1] = 1

            if i + 1 < n and j + 1 < m:
                dp[i][j][0] = (dp[i + 1][j][1] * dp[i + 1][j][0]) * (dp[i + 1][j + 1][1] + dp[i + 1][j + 1][0])
            elif i + 1 < n:
                dp[i][j][0] = dp[i + 1][j][1] + dp[i + 1][j][0]
            else:
                dp[i][j][0] = 1

for i in range(n):
    for j in range(m):
        print(dp[i][j][0], end=' ')
    print()
for i in range(n):
    for j in range(m):
        print(dp[i][j][1], end=' ')
    print()

ans = dp[0][0][0] + dp[0][0][1]
ans %= mod2
print(ans)
