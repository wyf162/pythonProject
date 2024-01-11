import sys

sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    x0, x1 = 0, 0
    y = 0
    for _ in range(n):
        s = input()
        x0 += s.count('0')
        x1 += s.count('1')
        y += len(s) // 2

    if y <= x0 // 2 + x1 // 2:
        print(n)
    else:
        print(n - 1)
