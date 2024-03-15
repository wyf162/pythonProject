import sys

# sys.stdin = open('./../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 10 ** 9 + 7

s = input()
ans = 0
a = 0
for c in s:
    if c == 'a':
        a += 1
    else:
        ans += pow(2, a, mod)
        ans -= 1
        ans %= mod
print(ans)
