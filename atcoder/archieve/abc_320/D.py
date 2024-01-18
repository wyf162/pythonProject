import sys
from collections import deque

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 10 ** 9 + 7

N, M = MI()
g = [[] for i in range(N)]
for _ in range(M):
    a, b, x, y = MI()
    a -= 1
    b -= 1
    g[a].append([b, x, y])
    g[b].append([a, -x, -y])

coords = [None for _ in range(N)]
q = deque()
q.append(0)
coords[0] = [0, 0]
while q:
    x = q.popleft()
    for y, dx, dy in g[x]:
        if coords[y] is None:
            coords[y] = [coords[x][0] + dx, coords[x][1] + dy]
            q.append(y)

for i in range(N):
    if coords[i]:
        print(coords[i][0], coords[i][1])
    else:
        print('undecidable')