import bisect
import sys

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 10 ** 9 + 7

n, m = MI()
a = LI()
b = LI()

a.sort()
b.sort()

l, r = 1, 10 ** 9 + 5
ans = 1
while l <= r:
    mid = (l + r) // 2
    i = bisect.bisect_right(a, mid)
    j = bisect.bisect_left(b, mid)
    if i >= m - j:
        ans = mid
        r = mid - 1
    else:
        l = mid + 1
print(ans)
