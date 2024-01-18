import sys
from heapq import heappush, heappop

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())

ret, k = MI()
B = []
for _ in range(k):
    b = []
    a = LI()
    a.pop(0)
    curr = 0
    min_seen = 0
    for x in a:
        curr += x
        min_seen = min(min_seen, curr)
        if curr > 0:
            b.append((min_seen, curr))
            min_seen = 0
            curr = 0
    b = b[::-1]
    if b:
        B.append(b)

h = []
for i in range(len(B)):
    heappush(h, (-B[i][-1][0], i))

while h:
    cand = heappop(h)[1]
    if B[cand][-1][0] + ret < 0:
        break
    ret += B[cand].pop()[1]
    if len(B[cand]):
        heappush(h, (-B[cand][-1][0], cand))
print(ret)
