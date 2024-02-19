# https://codeforces.com/problemset/problem/1200/E

import random
import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
# mod = 1000000007
# mod2 = 998244353

n = I()
ss = input().split()

N = 10 ** 6 + 5
times = random.randint(100, 500)
mod = random.getrandbits(32)
powers = [1] * (N + 1)
for i in range(1, N + 1):
    powers[i] = powers[i - 1] * times % mod

val1 = [0]
t = []
for s in ss:
    val2 = [0]
    for i, c in enumerate(s):
        val2.append((val2[-1] * times + ord(c)) % mod)

    x = min(len(t), len(s))
    while x > 0:
        if (val1[-1] - val1[-1 - x] * powers[x]) % mod == val2[x]:
            break
        x -= 1

    for i, c in enumerate(s[x:]):
        val1.append((val1[-1] * times + ord(c)) % mod)
        t.append(c)

print(''.join(t))
