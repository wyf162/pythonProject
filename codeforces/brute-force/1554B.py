import sys
# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = int(input())
for _tcn_ in range(tcn):
    n, k = MI()
    a = LI()
    l = max(0, n - 2 * k - 1)
    ans = -1e12
    for i in range(l, n):
        for j in range(i + 1, n):
            ans = max(ans, (i + 1) * (j + 1) - k * (a[i] | a[j]))
    print(ans)
