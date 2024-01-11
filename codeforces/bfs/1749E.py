import sys

sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())


def solve(grid):
    def check(i, j):
        ret = grid[i - 1][j] != '#' and grid[i + 1][j] != '#' and grid[i][j - 1] != '#' and grid[i][j + 1] != '#'
        return ret

    fa = [[m * n for _ in range(m + 2)] for _ in range(n + 2)]
    dp = [[m * n for _ in range(m + 2)] for _ in range(n + 2)]
    for j in [1]:
        for i in range(1, n + 1, 1):
            if grid[i][j] != '#' and check(i, j):
                dp[i][j] = 1
            elif grid[i][j] == '#':
                dp[i][j] = 0

    for j in range(2, m + 1, 1):
        for i in range(1, n + 1, 1):
            if grid[i][j] != '#' and check(i, j):
                if dp[i + 1][j - 1] < dp[i - 1][j - 1]:
                    dp[i][j] = dp[i + 1][j - 1] + 1
                    fa[i][j] = i + 1
                else:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    fa[i][j] = i - 1
            elif grid[i][j] == '#':
                if dp[i + 1][j - 1] < dp[i - 1][j - 1]:
                    dp[i][j] = dp[i + 1][j - 1]
                    fa[i][j] = i + 1
                else:
                    dp[i][j] = dp[i - 1][j - 1]
                    fa[i][j] = i - 1

    last_i = -1
    rst = m * n
    for j in [m]:
        for i in range(1, n + 1, 1):
            if dp[i][j] < rst:
                rst = dp[i][j]
                last_i = i

    if rst < m * n:
        for j in range(m, 0, -1):
            grid[last_i][j] = '#'
            last_i = fa[last_i][j]

    return rst


tcn = I()
for _tcn_ in range(tcn):
    n, m = MI()
    grid = [['.'] + list(input()) + ['.'] for _ in range(n)]
    grid.insert(0, ['.'] * (m + 2))
    grid.append(['.'] * (m + 2))
    grid2 = [row[::-1] for row in grid]

    rst1 = solve(grid)
    rst2 = solve(grid2)
    rst = min(rst1, rst2)

    if rst == m * n:
        print('NO')
    else:
        print('YES')
        if rst1 <= rst2:
            for i in range(1, n + 1, 1):
                print(''.join(grid[i][1:-1]))
        else:
            for i in range(1, n + 1, 1):
                print(''.join(reversed(grid2[i][1:-1])))
