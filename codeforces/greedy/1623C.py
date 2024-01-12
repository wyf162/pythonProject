import copy
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
    h = LI()


    def check(k):
        a = copy.deepcopy(h)
        for i in range(n - 1, 1, -1):
            if a[i] < mid:
                return False
            x = min(h[i], a[i] - mid)
            x //= 3
            a[i] -= 3 * x
            a[i - 1] += x
            a[i - 2] += x * 2
        if a[0] >= mid and a[1] >= mid:
            return True
        else:
            return False


    L, R = 0, max(h) + 1
    ans = 0
    while L <= R:
        mid = (L + R) // 2
        if check(mid):
            ans = mid
            L = mid + 1
        else:
            R = mid - 1
    print(ans)
