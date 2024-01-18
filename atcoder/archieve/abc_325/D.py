import sys
from collections import defaultdict
from heapq import heappop, heappush

sys.stdin = open('../../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())

N = I()

hst = defaultdict(list)
for _ in range(N):
    t, d = MI()
    hst[t].append(d)

h = []
ts = sorted(hst.keys())
cur_t = 1
rst = 0
for t in ts:
    while h and cur_t < t:
        if h[0] >= cur_t:
            rst += 1
            cur_t += 1
        heappop(h)

    for d in hst[t]:
        heappush(h, t + d)
    cur_t = max(cur_t, t)

while h:
    if h[0] >= cur_t:
        rst += 1
        cur_t += 1
    heappop(h)

print(rst)
