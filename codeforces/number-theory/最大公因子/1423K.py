import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

N = 10 ** 6 + 5
lpf = list(range(N))
for i in range(2, N):
    if lpf[i] == i:
        for j in range(i * i, N, i):
            lpf[j] = i

q = deque()
f = [0] * N
f[1] = 1
for i in range(2, N):
    if lpf[i] == i:
        q.append(i)
        f[i] = f[i - 1] + 1
    else:
        f[i] = f[i - 1]

    if q and q[0] * q[0] == i:
        q.popleft()
        f[i] -= 1

n = I()
A = LI()
for a in A:
    print(f[a])

