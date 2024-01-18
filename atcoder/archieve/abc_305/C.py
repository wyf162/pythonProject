import sys

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

H, W = MI()

mtx = ['.' + input() + '.' for _ in range(H)]
mtx.insert(0, '.' * (W + 2))
mtx.append('.' * (W + 2))

for i in range(1, H+1):
    for j in range(1, W+1):
        if mtx[i][j] == '.' and mtx[i][j + 1] == '#' and mtx[i][j - 1] == '#':
            exit(print(i, j))
        if mtx[i][j] == '.' and mtx[i - 1][j] == '#' and mtx[i + 1][j] == '#':
            exit(print(i, j))

        if mtx[i][j] == '.' and mtx[i + 1][j] == '#' and mtx[i][j + 1] == '#':
            exit(print(i, j))
        if mtx[i][j] == '.' and mtx[i + 1][j] == '#' and mtx[i][j - 1] == '#':
            exit(print(i, j))

        if mtx[i][j] == '.' and mtx[i - 1][j] == '#' and mtx[i][j + 1] == '#':
            exit(print(i, j))
        if mtx[i][j] == '.' and mtx[i - 1][j] == '#' and mtx[i][j - 1] == '#':
            exit(print(i, j))
