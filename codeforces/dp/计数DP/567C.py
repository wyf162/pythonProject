import math
import sys
from collections import Counter

# sys.stdin = open('./../input.txt', 'r')
# sys.stdout = open('./../output.txt', 'w')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, k = MI()
a = LI()

if k == 1:
    ans = 0
    cnt = Counter(a)
    for k, v in cnt.items():
        ans += math.comb(v, 3)
    exit(print(ans))

dp = dict()
for i in range(n):
    x = a[i]
    if x not in dp:
        dp[x] = [0, 0, 0]

    if x % k == 0:
        y = x // k
        if y in dp:
            dp[x][2] += dp[y][1]
            dp[x][1] += dp[y][0]
    dp[x][0] += 1

ans = 0
for k, v in dp.items():
    ans += v[2]
print(ans)
