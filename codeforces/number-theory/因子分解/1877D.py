import sys

# sys.stdin = open('./../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))
mod = 998244353

n = I()
a = LI()

lpf = list(range(n + 1))
for x in range(2, int(n ** .5) + 1):
    if lpf[x] == x:
        for y in range(x * x, n + 1, x):
            lpf[y] = x


def get_factors(x):
    facs = set()
    while x > 1:
        p = lpf[x]
        x //= p
        facs.add(p)
    return facs


f = [0] + a
for i in range(n, 0, -1):
    factors = get_factors(i)
    for x in factors:
        f[i // x] = max(f[i], f[i // x])

f.sort()
ans = 0
for i in range(1, n + 1):
    ans += f[i] * pow(2, i-1, mod)
    ans %= mod
print(ans)
