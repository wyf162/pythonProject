import copy
import sys
from collections import Counter

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

n = I()
a = LI()

dp = Counter()
# 0 1
# 00 01 10 11
# 000 001 010 011
# 100 101 110 111


for j in range(n):
    dpn = copy.deepcopy(dp)
    if a[j] % 2 == 1:
        # select
        dpn['1'] += 1
        dpn['01'] += dp['0']
        dpn['11'] += dp['1']
        # dpn['001'] += dp['00'] + dp['000'] + dp['100']
        dpn['011'] += dp['01'] + dp['001'] + dp['101']
        dpn['101'] += dp['10'] + dp['010'] + dp['110']
        # dpn['111'] += dp['11'] + dp['011'] + dp['111']

    else:
        # select
        dpn['0'] += 1
        dpn['00'] += dp['0']
        dpn['10'] += dp['1']
        dpn['000'] += dp['00'] + dp['000'] + dp['100']
        # dpn['010'] += dp['01'] + dp['001'] + dp['101']
        # dpn['100'] += dp['10'] + dp['010'] + dp['110']
        dpn['110'] += dp['11'] + dp['011'] + dp['111']

    dp = dpn
    for k, v in dp.items():
        dp[k] %= mod2

print(dp)
rst = 0
for k, v in dp.items():
    if len(k) == 3:
        rst += v

rst %= mod2
print(rst)
