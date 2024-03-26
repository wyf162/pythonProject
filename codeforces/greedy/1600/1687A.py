import sys

input = lambda: sys.stdin.readline().rstrip('\r\n')
sys.stdin = open('../../input.txt', 'r')
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
    n, k = MI()
    A = LI()
    pre_sum = [0] * (n + 1)
    for i in range(n):
        pre_sum[i + 1] = pre_sum[i] + A[i]
    if k < n:
        rst = 0
        for i in range(k, n + 1, 1):
            rst = max(rst, pre_sum[i] - pre_sum[i - k])
        rst += (k - 1) * k // 2
    else:
        rst = pre_sum[-1] + (n - 1) * n // 2 + n * (k - n)

    print(rst)
