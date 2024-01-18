import bisect
import sys

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
q = I()
queries = [LI() for _ in range(q)]

pre_sum = [0] * (n + 1)
for i in range(1, n):
    if i % 2 == 1:
        pre_sum[i] = pre_sum[i - 1]
    else:
        pre_sum[i] = pre_sum[i - 1] + a[i] - a[i - 1]

# print(pre_sum)
for query in queries:
    left, right = query
    i1 = bisect.bisect_left(a, left)
    i2 = max(bisect.bisect_left(a, right) - 1, 0)
    # print(i1, a[i1], i2, a[i2])
    ans = pre_sum[i2] - pre_sum[i1]
    if i1 % 2 == 0:
        ans += a[i1] - left
    if i2 % 2 == 1:
        ans += right - a[i2]
    print(ans)
