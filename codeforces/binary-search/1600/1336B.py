import bisect
import sys

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    n1, n2, n3 = MI()
    A = list(sorted(set(LI())))
    B = list(sorted(set(LI())))
    C = list(sorted(set(LI())))

    ans = 3 * 10 ** 18


    def solve(a, b, c):
        n1, n2, n3 = len(a), len(b), len(c)
        for j in range(n2):
            i = bisect.bisect_right(a, b[j])
            k = bisect.bisect_right(c, b[j])
            for di in [-1, 0, 1]:
                for dk in [-1, 0, 1]:
                    ni = i + di
                    nk = k + dk
                    ni = min(ni, n1 - 1)
                    ni = max(ni, 0)
                    nk = min(nk, n3 - 1)
                    nk = max(nk, 0)
                    # print(ni, j, nk)
                    x, y, z = a[ni], b[j], c[nk]
                    val = (x - y) * (x - y) + (x - z) * (x - z) + (y - z) * (y - z)
                    global ans
                    ans = min(ans, val)


    solve(A, B, C)
    solve(C, A, B)
    solve(A, C, B)
    print(ans)
