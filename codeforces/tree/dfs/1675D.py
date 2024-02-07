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
    root = -1
    tree = [[] for _ in range(n)]

    for i, x in enumerate(fa):
        if i == x:
            root = x
        else:
            tree[x].append(i)

    dep = [-1] * n
    stk = [root]
    while stk:
        x = stk.pop()
        for y in tree[x]:
            if dep[y] == -1:
                dep[y] = dep[x] + 1
                stk.append(y)

    vis = [0] * n
    sd = [(dep[x], x) for x in range(n)]
    sd.sort()
    ans = []
    for _, x in sd:
        if vis[x]:
            continue
        tmp = []
        while True:
            tmp.append(x)
            vis[x] = 1
            if tree[x]:
                x = tree[x].pop()
            else:
                break
        ans.append(tmp)
    print(len(ans))
    for tmp in ans:
        print(len(tmp))
        print(*[x+1 for x in tmp])
    print()
