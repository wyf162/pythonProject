import sys
from collections import Counter
from heapq import heappop, heappush

# sys.stdin = open('./../input.txt', 'r')
# sys.stdout = open('./../output.txt', 'w')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    a = LI()
    cnt = [0] * (n + 1)
    for v in a:
        cnt[v] += 1
    mx = max(cnt)
    val = cnt.count(mx)
    ans = ((n - val) // (mx - 1))
    print(ans - 1)
