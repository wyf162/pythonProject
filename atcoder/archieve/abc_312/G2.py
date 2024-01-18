import sys

sys.stdin = open('../../input.txt', 'r')
sys.setrecursionlimit(10 ** 6)

n = int(input())

mp = map(int, sys.stdin.read().split())
ab = list(zip(mp, mp))

graph = [[] for i in range(n + 1)]

for a, b in ab:
    graph[a].append(b)
    graph[b].append(a)

ans = [0]


def dfs(v, befv):
    tot = 1
    li = []
    for nv in graph[v]:
        if nv == befv:
            continue
        nvnum = dfs(nv, v)
        tot += nvnum
        li.append(nvnum)

    dp = [1, 0, 0, 0]
    for nu in li:
        for i in range(3)[::-1]:
            dp[i + 1] += dp[i] * nu

    ans[0] += dp[3]
    other = n - tot
    ans[0] += dp[2] * other

    return tot


dfs(1, 0)
print(ans[0])
