import sys
from collections import deque

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, h, l, r = MI()
a = LI()

f = [[-9] * h for i in range(n)]

k = a[0] % h
f[0][k] = int(l <= k <= r)

k = (a[0] - 1) % h
f[0][k] = int(l <= k <= r)

for i in range(n - 1):
    for j in range(h):
        if f[i][j] < 0:
            continue
        k = (j + a[i + 1]) % h
        f[i + 1][k] = max(f[i + 1][k], f[i][j] + int(l <= k <= r))

        k = (j + a[i + 1] - 1) % h
        f[i + 1][k] = max(f[i + 1][k], f[i][j] + int(l <= k <= r))

    # for j in range(h):
    #     if f[i][j] >= 0:
    #         print(j, end=' ')
    # print()
ans = max(f[-1])
print(ans)
