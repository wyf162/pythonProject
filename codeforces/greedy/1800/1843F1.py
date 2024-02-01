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
    n = I()
    events = [input().split() for _ in range(n)]
    mx = [0] * (n + 1)
    mi = [0] * (n + 1)
    mx_suf = [0] * (n + 1)
    mi_suf = [0] * (n + 1)
    mx[0] = 1
    mx_suf[0] = 1
    u = 0
    for event in events:
        if event[0] == '+':
            u += 1
            v, x = int(event[1]) - 1, int(event[2])
            mx_suf[u] = max(mx_suf[v] + x, 0)
            mi_suf[u] = min(mi_suf[v] + x, 0)
            mx[u] = max(mx[v], mx_suf[u])
            mi[u] = min(mi[v], mi_suf[u])
        else:
            v, k = int(event[2]) - 1, int(event[3])
            YN(mi[v] <= k <= mx[v])
