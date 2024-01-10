# -*- coding : utf-8 -*-
# @Time: 2023/12/3 19:46
# @Author: yefei.wang
# @File: C.py
import sys

sys.stdin = open('../../../input.txt')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

n, k, x = MI()

if n > k:
    exit(print(-1))

MI = n * (n + 1) // 2
MX = n * (k + k - n + 1) // 2
if x < MI or x > MX:
    exit(print(-1))


def get_mi_mx(n, k):
    return n * (n + 1) // 2, n * (k + k - n + 1) // 2


ans = []

while n > 0:
    print(n, k, x)
    l, r = 1, k
    y = r
    while l <= r:
        mid = (l + r) // 2
        mi, mx = get_mi_mx(n - 1, mid - 1)
        if x - mid < mi:
            r = mid - 1
        elif x - mid > mx:
            l = mid + 1
        else:
            y = mid
            break

    ans.append(y)
    n -= 1
    k = y - 1
    x -= y

print(*ans)
