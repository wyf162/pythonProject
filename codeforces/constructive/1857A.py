import sys

sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n, m = MI()
    mtx = [[0 for _ in range(m)] for _ in range(n)]
    s = 1
    for i in range(n):
        x = s << 8
        s += 1
        for j in range(m):
            mtx[i][j] = x + j
    #
    # for i in range(n - 4):
    #     for j in range(n - 4):
    #         y1 = mtx[i][j] ^ mtx[i + 1][j] ^ mtx[i][j + 1] ^ mtx[i + 1][j + 1]
    #         y2 = mtx[i + 2][j + 2] ^ mtx[i + 3][j + 2] ^ mtx[i + 2][j + 3] ^ mtx[i + 3][j + 3]
    #         print(y1, y2)
    print(n * m)
    for i in range(n):
        print(*mtx[i])
