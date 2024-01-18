import sys

sys.stdin = open('./../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

N, W = MI()
nwv = [LI() for _ in range(N)]

V = 10 ** 5 + 5
dp = [10 ** 12] * V
dp[0] = 0

for w, v in nwv:
    for kv in range(V - 1, v - 1, -1):
        dp[kv] = min(dp[kv], dp[kv - v] + w)

rst = 0
for i in range(V):
    if dp[i] <= W:
        rst = i
print(rst)
