import sys

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n = I()
a = LI()

s = sum(a)
if s % 2:
    exit(print(0))
K = s // 2
f = [[0] * (K + 1) for i in range(n + 1)]
f[0][0] = 1
for i in range(n):
    for j in range(K + 1):
        f[i + 1][j] |= f[i][j]
        if j + a[i] <= K:
            f[i + 1][j + a[i]] |= f[i][j]
if f[n][K] == 0:
    exit(print(0))
else:
    print(1)
    while True:
        for i in range(n):
            if a[i] % 2 == 1:
                exit(print(i + 1))
            a[i] //= 2
