import sys
from types import GeneratorType


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc


sys.stdin = open('../../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())

H, W = MI()
grid = [list(input()) for i in range(H)]


@bootstrap
def dfs(i, j):
    grid[i][j] = '.'
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == dj == 0:
                continue
            ni, nj = i + di, j + dj
            if 0 <= ni < H and 0 <= nj < W and grid[ni][nj] == '#':
                yield dfs(ni, nj)
    yield

ans = 0
for i in range(H):
    for j in range(W):
        if grid[i][j] == '#':
            dfs(i, j)
            ans += 1

print(ans)
