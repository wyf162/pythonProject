import sys

# sys.stdin = open('./../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    s1 = input()
    s2 = input()
    ops = []
    for i in range(n - 1):
        if s1[i] != s1[i + 1]:
            ops.append(i + 1)
    if s1[-1] != s2[-1]: ops.append(n)
    for i in range(n - 1, 0, -1):
        if s2[i] != s2[i - 1]:
            ops.append(i)
    print(len(ops), *ops)

