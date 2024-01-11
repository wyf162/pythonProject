import sys

sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    N = I()
    A = LI()
    suf = [0] * (N + 1)
    for i in range(N - 1, -1, -1):
        suf[i] = suf[i + 1] + A[i]

    ans = suf[0]
    for i in range(1, N, 1):
        if suf[i] > 0:
            ans += suf[i]
    print(ans)
