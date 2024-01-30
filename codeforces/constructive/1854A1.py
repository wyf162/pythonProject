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
    n = I()
    A = LI()
    mx, mi = max(A), min(A)
    if mx == mi:
        ops = []
    elif abs(mi) < mx:
        j = A.index(mx)
        ops = []
        for i in range(n):
            if A[i] > 0:
                continue
            A[i] += A[j]
            ops.append([i+1, j+1])
        for i in range(1, n):
            A[i] += A[i-1]
            ops.append([i+1, i])
    else:
        j = A.index(mi)
        ops = []
        for i in range(n):
            if A[i] < 0:
                continue
            A[i] += A[j]
            ops.append([i+1, j+1])
        for i in range(n-1, 0, -1):
            A[i-1] += A[i]
            ops.append([i, i+1])
    # print(A)
    print(len(ops))
    for i in range(len(ops)):
        print(*ops[i])

