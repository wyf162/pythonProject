import math
import sys

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))
mod = 10 ** 9 + 7

tcn, k = MI()
N = 100000 + 1
ans = [0] * N

for i in range(1, N):
    if i < k:
        ans[i] = ans[i - 1] + 1
    else:
        c = 0
        t = 0
        j = i
        while j >= c:
            t += math.comb(j, c)
            t %= mod
            j -= k - 1
            c += 1

        ans[i] = ans[i - 1] + t
    ans[i] %= mod

for _tcn_ in range(tcn):
    a, b = MI()
    rst = ans[b] - ans[a - 1]
    print(rst)
