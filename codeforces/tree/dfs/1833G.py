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
    g = [[] for _ in range(n)]

    for i in range(n - 1):
        u, v = GMI()
        g[u].append([v, i + 1])
        g[v].append([u, i + 1])

    if n % 3:
        print(-1)
        continue

    root = 0
    q = [0]
    fa = [-1] * n
    fa[0] = n
    tree = [[] for _ in range(n)]
    topo_sort = []

    while q:
        x = q.pop()
        topo_sort.append(x)
        for y, _ in g[x]:
            if fa[y] == -1:
                fa[y] = x
                tree[x].append(y)
                q.append(y)

    nums = [0] * n
    ans = []
    flag = True

    for x in topo_sort[::-1]:
        if x == root:
            continue
        if nums[x] == 0:
            nums[fa[x]] += 1
            if nums[fa[x]] > 2:
                flag = False
                break
        elif nums[x] == 1:
            if nums[fa[x]] == 0:
                nums[fa[x]] = 2
            else:
                flag = False
                break
        elif nums[x] == 2:
            for y, ind in g[x]:
                if y == fa[x]:
                    ans.append(ind)
        else:
            flag = False
            break
    if flag:
        print(len(ans))
        print(*ans)
    else:
        print(-1)
