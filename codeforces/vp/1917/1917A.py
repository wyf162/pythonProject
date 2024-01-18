import sys

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    a = LI()
    zero = pos = neg = 0
    for x in a:
        if x > 0:
            pos += 1
        elif x < 0:
            neg += 1
        else:
            zero += 1
    if zero:
        print(0)
        continue
    else:
        if neg % 2 == 0:
            print(1)
            print(1, 0)
        else:
            print(0)
