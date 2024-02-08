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
    left = -1
    for i in range(n):
        if A[i] > 1:
            left = i
            break
    right = n
    for i in range(n - 1, -1, -1):
        if A[i] > 1:
            right = i
            break
    if left == -1 and right == n:
        print(1, 1)
        continue

    tot = 1
    for i in range(left, right + 1):
        tot *= A[i]
        if tot > (1 << 60):
            break
    if tot > (1 << 60):
        print(left + 1, right + 1)
        continue

    idxs = []
    for i in range(n):
        if A[i] > 1:
            idxs.append(i)

    for i in range(len(idxs)):
        for j in range(i, len(idxs)):
            l, r = idxs[i], idxs[j]
            t = sum(A[:l]) + sum(A[r + 1:])
            v = 1
            for ii in range(l, r + 1):
                v *= A[ii]
            t += v
            if t > tot:
                tot = t
                left, right = l, r
    print(left + 1, right + 1)
