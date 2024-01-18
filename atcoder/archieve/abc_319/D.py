import itertools
import math
import sys

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 10 ** 9 + 7

N, M = MI()
A = LI()


def check(mid):
    k = 1
    line = -1
    for i in range(N):
        line += 1 + A[i]
        if line > mid:
            line = -1
            line += 1 + A[i]
            k += 1
    return k

l, r = max(A), 10**18
ans = r
while l<=r:
    mid = (l+r)//2
    if check(mid)<=M:
        ans = mid
        r = mid -1
    else:
        l = mid+1
print(ans)
