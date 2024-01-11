import sys
from collections import deque, Counter

# sys.stdin = open('./../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 10 ** 9 + 7

n, m, mx_t = MI()
g = [[] for _ in range(n)]
deg = [0] * n
for _ in range(m):
    u, v, w = MI()
    g[u - 1].append([v - 1, w])
    deg[v - 1] += 1

q = deque(i for i, d in enumerate(deg) if d == 0)
topo_sort = []
while q:
    x = q.popleft()
    topo_sort.append(x)
    for y, _ in g[x]:
        deg[y] -= 1
        if deg[y] == 0:
            q.append(y)

# print(topo_sort)
i = 0
while i < n and topo_sort[i] != 0:
    i += 1
topo_sort = topo_sort[i:]
# print(topo_sort)

dp = [Counter() for _ in range(n)]
dp[0][0] = [0, 0]
for x in topo_sort:
    for y, w in g[x]:
        for k, vv in dp[x].items():
            v, _ = vv
            if v + w > mx_t:
                continue
            if k + 1 not in dp[y]:
                dp[y][k + 1] = [v + w, x]
            elif dp[y][k + 1][0] > v + w:
                dp[y][k + 1] = [v + w, x]

step = max(dp[n - 1].keys())
print(step + 1)
ans = deque()
cur = n - 1
while step:
    ans.appendleft(cur)
    dis, pre = dp[cur][step]
    cur = pre
    step -= 1
ans.appendleft(0)

print(' '.join(map(lambda x: str(x + 1), ans)))
