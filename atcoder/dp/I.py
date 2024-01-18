import sys

sys.stdin = open('./../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(map(float, input().split()))
mod = 10 ** 9 + 7

n = I()
a = LI()
m = (n // 2) + 1
f = [[0 for i in range(n + 1)] for j in range(m)]
ans = 0
f[0][0] = 1

for i in range(n):
    ans += f[-1][i] * a[i]
    f[-1][i + 1] = 0

    for k in range(m):
        f[k][i + 1] += f[k][i] * (1 - a[i])

    for k in range(m - 1):
        f[k + 1][i + 1] += f[k][i] * a[i]

print(ans)
