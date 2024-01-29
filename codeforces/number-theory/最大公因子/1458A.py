import sys
import math

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

n, m = MI()
A = LI()
B = LI()
A.sort()
C = []
for i in range(1, n):
    C.append(A[i] - A[0])

x = 0
for c in C:
    x = math.gcd(x, c)

rst = []
for i in range(m):
    y = math.gcd(A[0]+B[i], x)
    rst.append(y)
print(rst)
