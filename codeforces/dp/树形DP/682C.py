import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

n = I()
A = LI()
g = [[] for _ in range(n)]
for x in range(1, n):
    y, w = MI()
    y -= 1
    g[x].append([y, w])
    g[y].append([x, w])

size = [1] * n
stk = [[0, -1, 0]]
while stk:
    x, fa, state = stk.pop()
    if state == 0:
        stk.append([x, fa, 1])
        for y, w in g[x]:
            if y != fa:
                stk.append([y, x, 0])
    else:
        for y, w in g[x]:
            if y != fa:
                size[x] += size[y]
print(size)
stk = [[0, -1]]
dist = [0] * n
ans = 0
while stk:
    x, fa = stk.pop()
    for y, w in g[x]:
        if y == fa:
            continue
        dist[y] = max(dist[x], 0) + w
        if dist[y] > A[y]:
            ans += size[y]
        else:
            stk.append([y, x])
print(ans)
