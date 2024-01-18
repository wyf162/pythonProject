import math
import sys

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

d = I()
ans = 10 ** 12

for x in range(10 ** 6 + 1):
    y = math.isqrt(abs(d - x * x))
    for y in (y + 1, y, y-1):
        ans = min(ans, abs(x * x + y * y - d))
print(ans)