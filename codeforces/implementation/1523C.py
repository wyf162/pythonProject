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
    a = [I() for _ in range(n)]
    seq = []
    for i in range(n):
        while True:
            if len(seq) == 0 or a[i] == 1:
                seq.append(a[i])
                break
            elif a[i] - seq[-1] == 1:
                seq[-1] = a[i]
                break
            seq.pop()
        print('.'.join(map(str, seq)))
