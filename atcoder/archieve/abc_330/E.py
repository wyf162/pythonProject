import sys
from collections import Counter
from heapq import heappop, heappush

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

n, q = MI()
a = LI()

cnt = Counter(a)

h = []
for i in range(n + 2):
    heappush(h, i)

for _ in range(q):
    i, x = MI()
    i -= 1
    prev = a[i]
    a[i] = x
    cnt[prev] -= 1
    cnt[x] += 1
    if cnt[prev] == 0:
        heappush(h, prev)

    while cnt[h[0]] != 0:
        heappop(h)
    print(h[0])
