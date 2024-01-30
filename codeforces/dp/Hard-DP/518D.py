import sys

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, q, t = input().split()
n = int(n)
q = float(q)
t = int(t)

dp1 = [[0 for _ in range(n)] for _ in range(t)]
dp2 = [[0 for _ in range(n)] for _ in range(t)]

dp1[0][0] = q
dp2[0][0] = 1 - q

for i in range(1, t, 1):
    for j in range(n):
        if j >= 1:
            dp1[i][j] = (dp1[i - 1][j - 1] + dp2[i - 1][j]) * q
        else:
            dp1[i][j] = dp2[i - 1][j] * q

        dp2[i][j] = dp2[i - 1][j] * (1 - q)

rst = sum(sum(row) for row in dp1)
print(rst)
