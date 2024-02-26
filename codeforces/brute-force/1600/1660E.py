import sys
from collections import Counter

input = lambda: sys.stdin.readline().rstrip('\r\n')
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
    input()
    n = I()
    mtx = [input() for _ in range(n)]
    c1, c0 = 0, 0
    for i in range(n):
        for j in range(n):
            if mtx[i][j] == '0':
                c0 += 1
            else:
                c1 += 1

    res = 0
    for i in range(n):
        k = 0
        for j in range(n):
            if mtx[j][(i + j) % n] == '1':
                k += 1
        res = max(res, k)
    ans = (n + c1 - 2 * res)
    print(ans)
