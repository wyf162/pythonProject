import sys

sys.stdin = open('./../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n = I()
h = LI()
d0 = 0
d1 = abs(h[1] - h[0])
for i in range(2, n):
    d0, d1 = d1, min(d1 + abs(h[i] - h[i - 1]), d0 + abs(h[i] - h[i - 2]))
print(d1)
