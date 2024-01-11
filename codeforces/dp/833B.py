import sys
from functools import lru_cache

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

N, K = MI()
A = LI()


@lru_cache(None)
def dfs(i, k):
    if k == 1:
        return len(set(A[:i + 1]))
    rst = 0
    s = set()
    s.add(A[i])
    for j in range(i - 1, k - 2, -1):
        rst = max(rst, dfs(j, k - 1) + len(s))
        s.add(A[j])
    return rst


ans = dfs(N - 1, K)
print(ans)
