import math
import sys

sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

n = I()
a = LI()
a.sort()
x1 = a.count(a[2])
x2 = a[:3].count(a[2])
ans = math.comb(x1, x2)
print(ans)
