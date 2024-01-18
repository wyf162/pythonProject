import sys

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

n = I()
courses = [LI() for _ in range(n)]
dp = [[0, 0]] * (n + 1)
for i in range(n):
    if courses[i][0] == 0:
        dp[i + 1][0] = max(dp[i][0] + courses[i][1], dp[i][1] + courses[i][1], dp[i][0])
        dp[i + 1][1] = dp[i][1]
    else:
        dp[i + 1][0] = dp[i][0]
        dp[i + 1][1] = max(dp[i][0] + courses[i][1], dp[i][1])

rst = max(dp[n])
print(rst)
