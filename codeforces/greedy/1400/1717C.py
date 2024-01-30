import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
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
    n = I()
    A = LI()
    B = LI()
    ans = True
    mx = max(B)
    i = B.index(mx)
    pre = False
    for _ in range(n):
        j1 = (i - 1) % n
        j2 = (i + 1) % n

        if A[i] > B[i]:
            ans = False
            break
        elif A[i] < B[i]:
            A[i] = B[i]
            cur = True
        else:
            cur = False

        if pre:
            if A[j1] - A[i] > 1:
                ans = False
                break

        pre = cur
        i += 1
        i %= n
    YN(ans)
