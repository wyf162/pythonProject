import sys

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

N, M = MI()

fact = [1] * (N + 1)
invfact = [1] * (N + 1)
for i in range(2, N + 1):
    fact[i] = fact[i - 1] * i % mod2

invfact[N] = pow(fact[N], mod2 - 2, mod2)
for i in range(N - 1, -1, -1):
    invfact[i] = invfact[i + 1] * (i + 1) % mod2


def choose(n, r):
    return fact[n] * invfact[r] % mod2 * invfact[n - r] % mod2


ans = 0
for k in range(N + 1):
    ans += (-1 if k % 2 else 1) * pow(M, max(1, N - k), mod2) * choose(N, k) % mod2

print(ans % mod2)
