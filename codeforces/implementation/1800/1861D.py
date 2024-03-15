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
    if n == 1:
        print(0)
        continue

    dp1 = [0 for _ in range(n)]
    dp2 = [0 for _ in range(n)]
    for i in range(1, n, 1):
        if a[i] <= a[i - 1]:
            dp1[i] = dp1[i - 1] + 1
        else:
            dp1[i] = dp1[i - 1]

        if a[i] >= a[i - 1]:
            dp2[i] = dp2[i - 1] + 1
        else:
            dp2[i] = dp2[i - 1]

    ans = min(dp1[-1], dp2[-1] + 1)
    for i in range(1, n, 1):
        ans = min(dp2[i - 1] + dp1[-1] - dp1[i] + 1, ans)
    print(ans)
