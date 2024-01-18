import itertools
import sys
import time

t1 = time.time()

sys.stdin = open('../../input.txt')

N, M, K = map(int, input().split())
edges = []
for _ in range(M):
    u, v, w = map(int, input().split())
    edges.append((u - 1, v - 1, w))

ans = K
for es in itertools.combinations(edges, N - 1):
    flag = [False] * N

    def dfs(x):
        flag[x] = True
        for u, v, _ in es:
            if u == x and not flag[v]:
                dfs(v)
            elif v == x and not flag[u]:
                dfs(u)

    dfs(0)
    if all(flag):
        cost = sum(w for _, _, w in es)
        ans = min(ans, cost % K)

print(ans)

t2 = time.time()
print(f"{t2-t1}s")