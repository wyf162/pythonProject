from collections import Counter

N = 10 ** 6
lpf = list(range(N + 1))
for x in range(2, int(N ** .5) + 1):
    if lpf[x] == x:
        for y in range(x * x, N + 1, x):
            lpf[y] = x


def get_factors(x):
    facs = []
    while x > 1:
        p = lpf[x]
        x //= p
        facs.append(p)
    return facs


import sys

# sys.stdin = open('./../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))
YN = lambda x: print('YES' if x else 'NO')
tcn = I()
for _tcn_ in range(tcn):
    n = I()
    a = LI()
    cnt = Counter()
    for i in range(n):
        facs = get_factors(a[i])
        for fac in facs:
            cnt[fac] += 1
    ans = True
    for k, v in cnt.items():
        if k > 1 and v % n:
            ans = False
            break
    YN(ans)
