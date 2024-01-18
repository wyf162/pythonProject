import sys
from collections import Counter

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 10 ** 9 + 7

n = I()
x = LI()
l = LI()

loc = []
for i in range(n):
    for j in range(n):
        loc.append(x[i] - l[j] - 1)
        loc.append(x[i] + l[j])

loc.sort()
curr = -10 ** 19
womais = 0
for xi in loc:
    dist = [abs(xi - x[i]) for i in range(n)]
    dist.sort()

    obama = all(dist[i] <= l[i] for i in range(n))
    if obama:
        womais += xi - curr
    curr = xi

print(womais)
