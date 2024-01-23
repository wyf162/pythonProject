import sys

# sys.stdin = open('./../input.txt', 'r')
input = lambda: sys.stdin.readline().rstrip('\r\n')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

# chip on board

tcn = I()
for _ in range(tcn):
    n = I()
    a = LI()
    b = LI()

    ans = min(min(a) * n + sum(b), min(b) * n + sum(a))
    print(ans)
