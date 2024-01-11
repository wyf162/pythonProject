import sys

sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    a = LI()
    pos = False
    for i in range(n):
        if a[i] > 0:
            pos = True
    ops = []

    if pos:
        mx = max(a)
        mxi = a.index(mx)
        for i in range(0, n - 1, 1):
            if a[i] <= a[i + 1]:
                continue
            while a[i] > a[i + 1]:
                a[i + 1] += mx
                ops.append([i + 1, mxi])
                if a[i + 1] > mx:
                    mx = a[i + 1]
                    mxi = i + 1
    else:
        mi = min(a)
        mii = a.index(mi)
        for i in range(n-2, -1, -1):
            if a[i] <= a[i+1]:
                continue
            while a[i] > a[i+1]:
                a[i] += mi
                ops.append([i, mii])
                if a[i] < mi:
                    mi = a[i]
                    mii = i
    # print(a)
    print(len(ops))
    for i in range(len(ops)):
        print(*[x+1 for x in ops[i]])