import sys

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

n = I()
a = LI()
ax = [(x, i) for i, x in enumerate(a)]
ax.sort()
ans = [-1] * n
max_right = -1
for x, i in ax:
    if max_right > i:
        ans[i] = max_right - i - 1
    max_right = max(max_right, i)

print(*ans)
