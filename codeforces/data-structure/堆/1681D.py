import sys
from heapq import heappop, heappush

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, x = MI()

q = []
heappush(q, (0, x))
ans = -1
vis = set()

while q:
    c, x = heappop(q)
    # print(c, x)
    s = str(x)
    for i in range(2, 10):
        if str(i) in s:
            if x * i not in vis:
                heappush(q, (c + 1, x * i))
                vis.add(x*i)
            if x * i >= 10 ** (n-1):
                ans = c + 1
                break
    if ans > 0:
        break
print(ans)
