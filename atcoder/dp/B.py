import sys

sys.stdin = open('./../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, K = MI()
h = LI()
f = [0x3f3f3f3f] * n
f[0] = 0
f[1] = abs(h[1] - h[0])
for i in range(2, n):
    for j in range(1, K+1):
        if i - j >= 0:
            f[i] = min(f[i], f[i - j] + abs(h[i] - h[i - j]))
print(f[-1])
