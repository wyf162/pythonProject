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
a = LI()
g = [[] for _ in range(n)]
for i in range(n - 1):
    u, v = GMI()
    g[u].append(v)
    g[v].append(u)

fa = [-1] * n
dfs = []
stk = [0]
while stk:
    x = stk.pop()
    dfs.append(x)
    for y in g[x]:
        if fa[x] != y:
            fa[y] = x
            stk.append(y)

# print(dfs)
# print(fa)


d = [0 for _ in range(n)]

for y in dfs[::-1]:
    d[y] += 1 if a[y] else -1
    if y:
        x = fa[y]
        d[x] += (d[y] if d[y] > 0 else 0)

for y in dfs:
    if y:
        x = fa[y]
        f, t = d[x], d[y]
        if t > 0:
            f -= t
        if f > 0:
            t += f
        d[y] = t

print(' '.join(map(str, d)))








