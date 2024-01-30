import sys
from functools import lru_cache

sys.setrecursionlimit(10 ** 6 + 5)
# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))
mod = 10 ** 9 + 7

n, K, d = MI()


@lru_cache(None)
def dfs(n, md):
    if n == 0:
        return int(md >= d)
    elif n < 0:
        return 0
    ret = 0
    for i in range(K, 0, -1):
        ret += dfs(n - i, max(md, i))
        ret %= mod
    return ret


rst = dfs(n, 0)
print(rst)
