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
    mtx = [LI() for _ in range(n)]
    s = [sum(row) for row in mtx]
    all_s = sum(s)
    if all_s % n:
        print(-1)
        continue
    goal_s = all_s // n
    ops = []
    for j in range(m):
        idx_big = [i for i in range(n) if s[i] > goal_s and mtx[i][j] == 1]
        for i in range(n):
            if s[i] >= goal_s:
                continue
            if s[i] < goal_s and idx_big and mtx[i][j] == 0:
                i1, i2 = i, idx_big.pop()
                ops.append([i1+1, i2+1, j+1])
                s[i1], s[i2] = s[i1] + 1, s[i2] - 1
                mtx[i1][j], mtx[i2][j] = mtx[i2][j], mtx[i1][j]
    print(len(ops))
    for i in range(len(ops)):
        print(*ops[i])
