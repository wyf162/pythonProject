import sys

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    n, m = MI()
    s = input()
    t = input()
    i = 0
    while i < 6:
        ss = s * (1 << i)
        if t in ss:
            print(i)
            break
        i += 1
    else:
        print(-1)
