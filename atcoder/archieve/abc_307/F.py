from collections import defaultdict
from heapq import *

n, m = map(int, input().split())
adj = defaultdict(list)
for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))

k = int(input())
A = list(map(int, input().split()))
D = int(input())
X = list(map(int, input().split()))

res = [-1] * (n + 1)
pq = []
for a in A:
    res[a] = 0
    for o, c in adj[a]:
        heappush(pq, (c, o))
# for each of the following days
for i, x in enumerate(X, 1):
    S = set()
    while pq:
        if pq[0][0] <= x:
            cost, who = heappop(pq)
            if res[who] != -1:
                continue
            else:
                res[who] = i
                for o, c in adj[who]:
                    if res[o] == -1:
                        heappush(pq, (cost + c, o))
                S.add(who)
        else:
            break
    for s in S:
        for o, c in adj[s]:
            if res[o] == -1:
                heappush(pq, (c, o))

for x in res[1:]:
    print(x)
