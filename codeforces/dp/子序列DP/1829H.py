import sys

# sys.stdin = open('./../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(map(int, input().split()))
mod = 10 ** 9 + 7

tcn = I()
for _tcn_ in range(tcn):
    n, k = MI()
    a = LI()
    f = [[0] * 64 for i in range(n + 1)]
    for i in range(n):
        f[i + 1][a[i]] = 1
        for j in range(64):
            f[i + 1][j] = (f[i + 1][j] + f[i][j]) % mod
            f[i + 1][j & a[i]] = (f[i + 1][j & a[i]] + f[i][j]) % mod

    rst = 0
    for i in range(64):
        if bin(i).count('1') == k:
            rst += f[-1][i]
            rst %= mod
    print(rst)
