import sys

sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n, iq = MI()
    a = LI()
    s = nq = 0
    b = ['0'] * n
    for i in range(n)[::-1]:
        if a[i] <= nq:
            b[i] = '1'
        elif nq < iq:
            nq += 1
            b[i] = '1'
        else:
            b[i] = '0'

    print("".join(b))
