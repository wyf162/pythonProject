import sys

input = lambda: sys.stdin.readline().rstrip()
mi = lambda: map(int, input().split())
li = lambda: list(mi())

N, M = mi()
cost = []
roulette = []
for i in range(N):
    c, p, *S = mi()
    cost.append(c)
    roulette.append(S)

dp = [0] * (2 * M + 1)
for x in range(1, 2 * M + 1):
    dp[x] = 10 ** 100
    for i in range(N):
        n = len(roulette[i])
        tmp = cost[i]
        zero = 0
        for j in range(n):
            if roulette[i][j] == 0:
                zero += 1
            elif 0 <= x - roulette[i][j]:
                tmp += dp[x - roulette[i][j]] / n
        tmp = (n / (n - zero)) * tmp
        dp[x] = min(dp[x], tmp)

print(min(dp[M:]))


