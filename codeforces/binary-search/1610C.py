import sys

input = lambda: sys.stdin.readline().rstrip()
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
    n = I()
    ab = [LI() for _ in range(n)]


    def check(x):
        c = 0
        for i in range(n):
            a, b = ab[i]
            if x - 1 - c <= a and b >= c:
                c += 1
        return c >= x


    L, R = 1, n
    while L <= R:
        mid = (L + R) // 2
        if check(mid):
            ans = mid
            L = mid + 1
        else:
            R = mid - 1
    print(ans)
