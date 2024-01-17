import sys

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

tcn = I()
for _tcn_ in range(tcn):
    n, m = MI()
    nums = LI()
    vi = [(v, i) for i, v in enumerate(nums)]
    vi.sort(key=lambda x: x[0])
    mtx = []
    for i in range(n):
        mtx.append(vi[m * i: m * i + m])
        mtx[i].sort(key=lambda x: (x[0], -x[1]))

    # for i in range(n):
    #     print(mtx[i])

    ans = 0
    for i in range(n):
        for j in range(m):
            s = mtx[i][j][1]
            for k in range(j):
                if mtx[i][k][1] < s:
                    ans += 1
    print(ans)
