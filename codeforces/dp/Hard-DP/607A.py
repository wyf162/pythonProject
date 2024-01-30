import bisect
import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

n = I()
pp = [LI() for _ in range(n)]
pp.sort()
A = [a for a, b in pp]

left = [-1] * n
for i in range(1, n):
    j = bisect.bisect_left(A, pp[i][0] - pp[i][1])
    left[i] = j - 1

print(left)

dp = [1] * n
for i in range(n - 1, -1, -1):
    j = left[i]
    if j >= 0:
        dp[j] = max(dp[j], dp[i] + 1)

print(n - max(dp))
