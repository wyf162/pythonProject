import sys

input = lambda: sys.stdin.readline().rstrip('\r\n')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _ in range(tcn):
    n = I()
    a = []
    for i in range(n):
        a.append(LI())

    l, r = 1, a[0][0]
    for i in range(1, n):
        if a[i][1] >= a[0][1]:
            l = max(l, a[i][0] + 1)
    if l <= r:
        print(l)
    else:
        print(-1)
