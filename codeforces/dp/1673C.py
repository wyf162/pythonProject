import sys

# sys.stdin = open('./../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))
mod = 10 ** 9 + 7

N = 4 * 10 ** 4 + 4
p = []

for i in range(1, N):
    s = str(i)
    j = 0
    ans = True
    while j * 2 < len(s):
        if s[j] == s[-j - 1]:
            j += 1
            continue
        else:
            ans = False
            break
    if ans:
        p.append(i)

print(len(p))
M = len(p)
dp = [0] * N
dp[0] = 1
for j in range(M):
    for i in range(1, N):
        if i >= p[j]:
            dp[i] += dp[i - p[j]]
            dp[i] %= mod

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    print(dp[n])
