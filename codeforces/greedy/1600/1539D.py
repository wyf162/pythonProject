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

n = I()
ab = [LI() for _ in range(n)]

ab.sort(key=lambda x: x[1])
tot = sum(x[0] for x in ab)

ans = cur = 0
for i in range(n):
    if cur >= tot:
        break
    if ab[i][1] >= tot:
        break
    cur = max(cur, ab[i][1])
    add = min(ab[i][0], tot - cur)
    ans += add
    cur += add

print(tot * 2 - ans)
