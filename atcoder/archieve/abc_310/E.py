import sys

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

n = I()
a = [int(x) for x in input()]

ans = 0
z, o = 0, 0
for x in a:
    if x == 0:
        z, o = 1, z + o
    elif x == 1:
        z, o = o, z + 1
    ans += o

print(ans)
