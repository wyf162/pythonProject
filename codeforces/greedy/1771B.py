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

tcn = I()
for _tcn_ in range(tcn):
    n, m = MI()
    pairs = [sorted(LGMI()) for _ in range(m)]
    upper = [n - 1] * n
    for x, y in pairs:
        upper[x] = min(upper[x], y - 1)
    for i in range(n - 2, -1, -1):
        upper[i] = min(upper[i], upper[i + 1])
    print(sum(v - i + 1 for i, v in enumerate(upper)))
