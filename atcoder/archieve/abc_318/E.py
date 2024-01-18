import sys
from collections import Counter

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 10 ** 9 + 7

n = I()
a = LI()

hst = dict()
cnt = Counter()
dp = [0] * n

for i, x in enumerate(a):
    if x not in hst:
        hst[x] = i
        cnt[x] += 1
    else:
        dp[i] = (i - hst[x] - 1) * cnt[x] + dp[hst[x]]
        hst[x] = i
        cnt[x] += 1
print(sum(dp))
