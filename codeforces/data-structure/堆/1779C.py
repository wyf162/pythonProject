import sys
from heapq import heappop, heappush

sys.stdin = open('../../input.txt', 'r')
sys.stdout = open('../../output.txt', 'w')
input = lambda: sys.stdin.readline().rstrip('\r\n')

I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n, m = MI()
    a = LI()
    pre_sum = [0] * (n + 1)
    for i in range(n):
        pre_sum[i + 1] = pre_sum[i] + a[i]

    ans = 0

    h = [-a[m - 1]]
    tot = pre_sum[m]
    for i in range(m - 1)[::-1]:
        while pre_sum[i + 1] < tot:
            x = heappop(h)
            tot += 2 * x
            ans += 1
        heappush(h, -a[i])

    h = []
    tot = 0
    for i in range(m, n, 1):
        tot += a[i]
        heappush(h, a[i])
        while tot < 0:
            x = heappop(h)
            tot += 2 * (-x)
            ans += 1
    print(ans)
