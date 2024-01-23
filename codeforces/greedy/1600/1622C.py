import math
import sys


input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353
# sys.stdout = open('../output1.txt', 'w')

tcn = I()
for _tcn_ in range(tcn):
    n, k = MI()
    a = LI()
    a.sort()
    pre_sum = [0] * (n + 1)
    for i in range(n):
        pre_sum[i + 1] = pre_sum[i] + a[i]
    if pre_sum[n] <= k:
        print(0)
        continue

    ans = 10 ** 16
    for y in range(n):
        x = max(a[0] - math.floor((k - pre_sum[n - y] + a[0]) / (y + 1)), 0)
        ans = min(ans, x + y)
    print(ans)
