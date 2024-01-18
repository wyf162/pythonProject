import sys
from collections import defaultdict, Counter, deque

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

n1, n2, m = MI()
g1 = defaultdict(list)
g2 = defaultdict(list)

for _ in range(m):
    u, v = MI()
    if u <= n1:
        g1[u].append(v)
        g1[v].append(u)
    else:
        g2[u].append(v)
        g2[v].append(u)

dist1 = Counter()
dist2 = Counter()

dist1[1] = 0
dist2[n1 + n2] = 0

q1 = deque()
q1.append(1)
while q1:
    x = q1.popleft()
    for y in g1[x]:
        if y not in dist1:
            dist1[y] = dist1[x] + 1
            q1.append(y)
        else:
            dist1[y] = min(dist1[y], dist1[x] + 1)


q2 = deque()
q2.append(n1+n2)
while q2:
    x = q2.popleft()
    for y in g2[x]:
        if y not in dist2:
            dist2[y] = dist2[x] + 1
            q2.append(y)
        else:
            dist2[y] = min(dist2[y], dist2[x] + 1)

rst = max(dist1.values()) + max(dist2.values()) + 1
print(rst)
