import sys
from itertools import permutations

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

n, m = MI()
s = input()

perms = list(permutations('abc'))
acc = [[0] * (n + 1) for _ in range(6)]

for i in range(n):
    for j in range(6):
        if s[i] != perms[j][i % 3]:
            acc[j][i + 1] = acc[j][i] + 1
        else:
            acc[j][i + 1] = acc[j][i]

for _ in range(m):
    l, r = GMI()
    print(min(acc[i][r + 1] - acc[i][l] for i in range(6)))