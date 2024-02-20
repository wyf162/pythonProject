# https://codeforces.com/problemset/problem/1730/C

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

tcn = I()
for _tcn_ in range(tcn):
    nums = [int(x) for x in input()]
    n = len(nums)
    f = [9] * n
    f[n - 1] = nums[n - 1]
    for i in range(n - 2, -1, -1):
        f[i] = min(f[i + 1], nums[i])

    ans = []
    for i in range(n):
        if nums[i] > f[i]:
            ans.append(min(nums[i] + 1, 9))
        else:
            ans.append(nums[i])
    ans.sort()
    print(''.join(str(x) for x in ans))
