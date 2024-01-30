import sys

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))
mod = 10 ** 9 + 7

s = input()
n = len(s)
# *, 0, *1, 1*, 2
f = [[0, 0, 0, 0, 0] for _ in range(n)]

if s[0] == '?':
    f[0] = [1, 1, 0, 1, 0]
elif s[0] == '0':
    f[0] = [0, 1, 0, 0, 0]
elif s[0] == '1':
    f[0] = [0, 0, 0, 1, 0]
elif s[0] == '2':
    f[0] = [0, 0, 0, 0, 0]
elif s[0] == '*':
    f[0] = [1, 0, 0, 0, 0]

for i in range(1, n):
    if s[i] == '?':
        f[i][0] = f[i - 1][0] + f[i - 1][3] + f[i - 1][4]
        f[i][1] = f[i - 1][1] + f[i - 1][2]
        f[i][2] = f[i - 1][0]
        f[i][3] = f[i - 1][1] + f[i - 1][2]
        f[i][4] = f[i - 1][0]
    elif s[i] == '0':
        f[i][1] = f[i - 1][1] + f[i - 1][2]
    elif s[i] == '1':
        f[i][2] = f[i - 1][0]
        f[i][3] = f[i - 1][1] + f[i - 1][2]
    elif s[i] == '2':
        f[i][4] = f[i - 1][0]
    elif s[i] == '*':
        f[i][0] = f[i - 1][0] + f[i - 1][3] + f[i - 1][4]

    for j in range(5):
        f[i][j] %= mod

rst = f[-1][0] + f[-1][1] + f[-1][2]
rst %= mod
print(rst)
