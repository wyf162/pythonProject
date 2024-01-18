import sys

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

n, k = MI()

abs = [LI() for _ in range(n)]
abs.sort()

s = sum(ab[1] for ab in abs)
if s <= k:
    exit(print(1))

for a, b in abs:
    s -= b
    if s <= k:
        print(a + 1)
        break
