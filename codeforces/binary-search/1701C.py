import sys
from collections import Counter

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
    n, m = MI()
    a = LI()
    # 被卡hash 先sort.
    a.sort()
    cnt = Counter(a)


    def check(x):
        c = 0
        for i in range(1, n + 1):
            if cnt[i] >= x:
                c += x
            else:
                c += cnt[i] + (x - cnt[i]) // 2
            if c >= m:
                return True
        return False


    L, R = 0, 10 ** 6
    while L <= R:
        mid = (L + R) // 2
        if check(mid):
            ans = mid
            R = mid - 1
        else:
            L = mid + 1
    print(ans)
