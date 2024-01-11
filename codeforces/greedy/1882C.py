import sys
# sys.stdin = open('./../input.txt', 'r')
input = lambda: sys.stdin.readline().rstrip('\r\n')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

# card game
tcn = I()
for _tcn_ in range(tcn):
    n = I()
    a = LI()

    if n == 1:
        print(max(a[0], 0))
        continue
    g = max(0, a[0], a[0] + a[1])
    for i in range(2, n):
        g += max(a[i], 0)
    print(g)
