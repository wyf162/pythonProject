import sys

sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353


class LeastPrimeFactor:

    def __init__(self, n):
        self.N = n
        self.lpf = list(range(self.N + 1))
        for x in range(2, int(self.N ** .5) + 1):
            if self.lpf[x] == x:
                for y in range(x * x, self.N + 1, x):
                    self.lpf[y] = x

    def is_prime(self, x):
        return self.lpf[x] == x


MX = 10 ** 5 + 5
pf = LeastPrimeFactor(MX)

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    a = LI()
    ans = False
    for x in range(2, MX):
        if x * x > 1e9:
            break
        if not pf.is_prime(x):
            continue
        cnt = 0
        for i in range(n):
            if a[i] % x == 0:
                cnt += 1
        if cnt >= 2:
            ans = True
            break
    if ans:
        print('YES')
    else:
        print('NO')
