import sys

sys.stdin = open('./../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, k = MI()
a = LI()
mod = 10 ** 9 + 7

f = [[0 for j in range(k + 1)] for i in range(n + 1)]
s = [[0 for j in range(k + 1)] for i in range(n + 1)]

f[1][0] = s[1][0] = 1
for i in range(1, k + 1):
    f[1][i] = int(i <= a[0])
    s[1][i] = f[1][i] + s[1][i - 1]

for i in range(2, n + 1, 1):
    f[i][0] = s[i][0] = 1
    for j in range(1, k + 1):
        if j <= a[i - 1]:
            f[i][j] = s[i - 1][j] % mod
        else:
            f[i][j] = s[i - 1][j] - s[i - 1][j - a[i - 1] - 1]
            f[i][j] %= mod
        s[i][j] = s[i][j - 1] + f[i][j]
        s[i][j] %= mod
print(f[-1][-1])
