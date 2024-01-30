import sys
from itertools import accumulate

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
    n, k = MI()
    prices = LI()
    pre_sum = [0] + list(accumulate(prices))
    rst = 0
    for i in range(n):
        r = (n - i) // k
        rst = max(rst, pre_sum[i+r] - pre_sum[i])
    print(rst)
