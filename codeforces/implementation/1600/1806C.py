import sys

sys.stdin = open('../../input.txt', 'r')
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
    rst = sum(abs(x) for x in a)
    if n == 1:
        rst = min(rst, abs(a[1] - a[0]))
    if n == 2:
        rst = min(rst, sum(abs(x - 2) for x in a))
    if n % 2 == 0:
        tot = 0
        for i in range(2 * n):
            tot += abs(a[i] + 1)
        for i in range(2 * n):
            t = tot - abs(a[i] + 1) + abs(a[i] - n)
            rst = min(rst, t)

    print(rst)
