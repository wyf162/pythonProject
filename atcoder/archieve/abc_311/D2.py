import sys
from collections import deque

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

n, m = MI()
grid = [list(input()) for i in range(n)]

vis = [[0 for j in range(m)] for i in range(n)]

q = deque()
q.append((1, 1))
points = set()
while q:
    x, y = q.popleft()
    points.add((x, y))
    for ny in range(y+1, m):
        # if vis[x][ny]:
        #     break
        if grid[x][ny] == '.':
            vis[x][ny] = 1
        else:
            if (x, ny - 1) not in points:
                q.append((x, ny - 1))
            break
    for ny in range(y, -1, -1):
        # if vis[x][ny]:
        #     break
        if grid[x][ny] == '.':
            vis[x][ny] = 1
        else:
            if (x, ny + 1) not in points:
                q.append((x, ny + 1))
            break

    for nx in range(x+1, n):
        # if vis[nx][y]:
        #     break
        if grid[nx][y] == '.':
            vis[nx][y] = 1
        else:
            if (nx - 1, y) not in points:
                q.append((nx - 1, y))
            break
    for nx in range(x, -1, -1):
        # if vis[nx][y]:
        #     break
        if grid[nx][y] == '.':
            vis[nx][y] = 1
        else:
            if (nx + 1, y) not in points:
                q.append((nx + 1, y))
            break

rst = sum(vis[i].count(1) for i in range(n))
print(rst)
