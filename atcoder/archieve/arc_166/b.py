import math

n, a, b, c = map(int, input().split())
A = list(map(int, input().split()))

dp = [[5 * 10 ** 18] * 8 for i in range(n + 1)]
dp[0][0] = 0

r = [a, b, c]
d = [1, 1, 1, 1, 1, 1, 1, 1]

for i in range(8):
    for j in range(3):
        if i >> j & 1:
            d[i] = r[j] // math.gcd(d[i], r[j]) * d[i]

# print(d)

for i in range(n):
    for j in range(8):
        t = (-A[i]) % d[j]
        for k in range(8):
            dp[i + 1][j | k] = min(dp[i + 1][j | k], dp[i][k] + t)

print(dp[n][7])
