import sys
from collections import Counter

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

n, t, m = MI()

hate = [0] * n
teams = []
for _ in range(m):
    a, b = MI()
    hate[b - 1] |= 1 << (a - 1)


def dfs(now):
    if now == n:
        return len(teams) == t

    ans = 0

    for i, team in enumerate(teams):
        if not (team & hate[now]):
            teams[i] ^= 1 << now
            ans += dfs(now + 1)
            teams[i] ^= 1 << now

    if len(teams) < t:
        teams.append(1 << now)
        ans += dfs(now + 1)
        teams.pop()

    # print(f'now = {now}, teams = {teams}')
    return ans


print(dfs(0))
