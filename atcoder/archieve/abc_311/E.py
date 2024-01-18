import sys

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

h, w, n = MI()
MX = 3005
dp = [[0 for i in range(3005)] for i in range(3005)]
hole = [[0 for i in range(3005)] for i in range(3005)]

for _ in range(n):
    i, j = MI()
    hole[i][j] = 1
ans = 0
for i in range(1, h + 1):
    for j in range(1, w + 1):
        if hole[i][j]:
            continue
        dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
        ans += dp[i][j]
print(ans)
