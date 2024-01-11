def comb(n, k, mod):
    num = 1
    for i in range(n - k + 1, n + 1):
        num *= i
        num %= mod

    den = 1
    for i in range(2, k + 1):
        den *= i
        den %= mod

    res = num * pow(den, mod - 2, mod)
    return res % mod


# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))
mod = 998244353

n, m = MI()

ans = comb(m, n - 1, mod)
ans %= mod
ans *= (n - 2)
ans %= mod
ans *= pow(2, n - 3, mod)
ans %= mod
print(ans)
