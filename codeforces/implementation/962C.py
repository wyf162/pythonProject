import math
import sys

sys.stdin = open('../input.txt')

a = [int(c) for c in input()]
n = len(a)
rst = -1
for i in range(1, 1 << n, 1):
    x = 0
    for b in range(n):
        if i >> b & 1:
            x = x * 10 + a[b]
    # print(x)
    y = math.isqrt(x)
    if 0 < x == y * y:
        rst = max(rst, len(str(x)))

if rst > 0:
    print(n - rst)
else:
    print(rst)
