import bisect
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
    tree = [[] for _ in range(n)]
    for i in range(1, n):
        fa, a, b = MI()
        fa -= 1
        tree[fa].append([i, a, b])

    ans = [0] * n
    pre_sa = []
    pre_sb = []
    stk = [[0, 0, 0, 0]]
    while stk:
        x, state, a, b = stk.pop()
        if state == 0:
            stk.append([x, 1, a, b])
            if x == 0:
                pre_sa.append(a)
                pre_sb.append(b)
            else:
                pre_sa.append(pre_sa[-1] + a)
                pre_sb.append(pre_sb[-1] + b)
            # print(x, pre_sa, pre_sb)
            i = bisect.bisect_right(pre_sb, pre_sa[-1])
            ans[x] = i - 1
            for y, a, b in tree[x]:
                stk.append([y, 0, a, b])
        else:
            pre_sa.pop()
            pre_sb.pop()

    print(*ans[1:])
