import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('./../input.txt', 'r')
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
C1 = [[[0, 0, 0]] for _ in range(m + 1)]
C2 = [[[0, 0, 0]] for _ in range(m + 1)]
rst = 0
for i in range(n):
    c = B[i]
    if i % 2 == 1:
        if len(C1[c]) >= 2:
            k = len(C1[c]) - 1
            rst += C1[c][-1][2] + C1[c][-1][0] * A[i] + C1[c][-1][1] * (i + 1) + (i + 1) * A[i] * k
            rst = rst % 100007

        x, y, z = C1[c][-1][0] + i + 1, C1[c][-1][1] + A[i], C1[c][-1][2] + (i + 1) * A[i]
        C1[c].append([x, y, z])
    else:
        if len(C2[c]) >= 2:
            k = len(C2[c]) - 1
            rst += C2[c][-1][2] + C2[c][-1][0] * A[i] + C2[c][-1][1] * (i + 1) + (i + 1) * A[i] * k
            rst = rst % 100007

        x, y, z = C2[c][-1][0] + i + 1, C2[c][-1][1] + A[i], C2[c][-1][2] + (i + 1) * A[i]
        C2[c].append([x, y, z])

rst = rst % 100007

print(rst)
