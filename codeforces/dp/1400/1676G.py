import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    fa = LGMI()
    s = input()

    tree = [[] for _ in range(n)]
    for i, x in enumerate(fa, start=1):
        tree[x].append(i)

    fa = [-1] + fa
    dfs = []
    stk = [0]
    while stk:
        x = stk.pop()
        dfs.append(x)
        for y in tree[x]:
            stk.append(y)

    dp = [0] * n
    for x in dfs[::-1]:
        if s[x] == 'B':
            dp[x] += 1
        else:
            dp[x] -= 1

        if fa[x] >= 0:
            dp[fa[x]] += dp[x]
    ans = dp.count(0)
    print(ans)
