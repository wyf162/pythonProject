import sys

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 10 ** 9 + 7

N = I()
mtx = [LI() for i in range(N-1)]

f = [0] * (1 << N)
for i in range(N):
    for j in range(i + 1, N):
        s = (1 << i) | (1 << j)
        f[s] = mtx[i][j - i - 1]

for s in range((1 << N)):
    k = s
    while k > 0:
        k = s & (k - 1)
        f[s] = max(f[s], f[k] + f[s - k])

mx = max(f)
print(mx)
