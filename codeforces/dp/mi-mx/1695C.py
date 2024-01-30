import sys

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    m, n = MI()
    grid = [LI() for _ in range(m)]
    if (m + n) % 2 == 0:
        print('NO')
        continue

    fmx = [[0 for j in range(n)] for i in range(m)]
    fmx[0][0] = grid[0][0]
    for j in range(1, n):
        fmx[0][j] = fmx[0][j - 1] + grid[0][j]
    for i in range(1, m):
        fmx[i][0] = fmx[i - 1][0] + grid[i][0]

    for i in range(1, m):
        for j in range(1, n):
            fmx[i][j] = max(fmx[i - 1][j], fmx[i][j - 1]) + grid[i][j]

    fmi = [[0 for j in range(n)] for i in range(m)]
    fmi[0][0] = grid[0][0]
    for j in range(1, n):
        fmi[0][j] = fmi[0][j - 1] + grid[0][j]
    for i in range(1, m):
        fmi[i][0] = fmi[i - 1][0] + grid[i][0]

    for i in range(1, m):
        for j in range(1, n):
            fmi[i][j] = min(fmi[i - 1][j], fmi[i][j - 1]) + grid[i][j]

    if fmi[m - 1][n - 1] <= 0 <= fmx[m - 1][n - 1]:
        print('YES')
    else:
        print('NO')
