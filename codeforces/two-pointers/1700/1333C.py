import sys
from collections import Counter

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n = I()
a = LI()

hst = dict()
hst[0] = -1
left = -1
pre_sum = 0
ans = 0
for i in range(n):
    if a[i] == 0:
        left = i
        continue

    pre_sum += a[i]
    if pre_sum in hst:
        left = max(left, hst[pre_sum] + 1)

    hst[pre_sum] = i
    ans += i - left
    if pre_sum == 0:
        left = max(left, pre_sum)
print(ans)
