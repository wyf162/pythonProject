import sys
from collections import defaultdict

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 10 ** 9 + 7

n = I()
hst = defaultdict(list)
for _ in range(n):
    f, s = MI()
    hst[f].append(s)

ans = 0
mx = 0
for k, v in hst.items():
    v.sort(reverse=True)
    ans = max(ans, v[0] + mx)
    if len(v) > 1:
        ans = max(ans, v[0] + v[1] // 2)
    mx = max(mx, v[0])
print(ans)
