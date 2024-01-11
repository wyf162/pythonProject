import math
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
    L, R = MI()
    mxl = 0
    while L * (1 << mxl) <= R:
        mxl += 1
    print(mxl, end=' ')
    if mxl == 1:
        print(R - L + 1)
    else:
        p1 = 2 ** (mxl - 1)
        p2 = 2 ** (mxl - 2)
        r1 = R // p1
        r2 = R // (p2 * 3)
        ans = (r1 - L + 1)
        if r2 >= L:
            ans += (r2 - L + 1) * (mxl - 1)
        ans %= mod2
        print(ans)
