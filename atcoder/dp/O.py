import sys

sys.stdin = open('./../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(map(int, input().split()))
mod = 10 ** 9 + 7

N = I()
grid = [LI() for _ in range(N)]

PN = 1 << N
dp = [[0 for j in range(PN)] for i in range(N + 1)]
group = [[] for i in range(N + 1)]

# 分组后可以优化掉一个n，时间复杂度大概是n*2**n
for i in range(PN):
    x = bin(i).count('1')
    group[x].append(i)

dp[0][0] = 1
for i in range(1, N + 1):
    for k in group[i - 1]:
        for j in range(N):
            if grid[i - 1][j] == 1 and (k >> j & 1) == 0:
                dp[i][k | (1 << j)] += dp[i - 1][k]
                dp[i][k | (1 << j)] %= mod

rst = dp[N][PN - 1]
print(rst)
