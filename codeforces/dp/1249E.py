import sys

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, c = MI()
a = LI()
b = LI()

fa = [0] * n
fb = [c] * n
fc = [0] * n
for i in range(1, n):
    fa[i] = min(fa[i - 1] + a[i - 1], fb[i - 1] + a[i - 1])
    fb[i] = min(fb[i - 1] + b[i - 1], fa[i - 1] + b[i - 1] + c)
    fc[i] = min(fa[i], fb[i])

print(' '.join(map(str, fc)))
