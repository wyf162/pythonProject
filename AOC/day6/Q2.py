import sys

sys.stdin = open('./input.txt', 'r')
# sys.stdin = open('./i1.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

ts = int(''.join(x for x in input().split()[1:]))
dists = int(''.join(x for x in input().split()[1:]))
print(ts)
print(dists)

rst = 0
for i in range(ts + 1):
    td = i * (ts - i)
    if td > dists:
        rst += 1

print(rst)
