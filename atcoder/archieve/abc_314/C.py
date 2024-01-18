import sys

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 10 ** 9 + 7

n, m = MI()
s = input()
c = LI()

g = [[] for i in range(m + 1)]
f = [[] for i in range(m + 1)]
for i in range(n):
    g[c[i]].append(s[i])
    f[c[i]].append(i)

for i in range(1, m + 1):
    g[i].insert(0, g[i].pop())

ans = [''] * n
for i in range(1, m + 1):
    for j, k in enumerate(f[i]):
        ans[k] = g[i][j]

print(''.join(ans))
