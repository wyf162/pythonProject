import sys

input = lambda: sys.stdin.readline().rstrip()
# sys.stdin = open('../input.txt', 'r')
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
    n, m = MI()
    A = []
    cnt = [0] * (n + 1)
    ans = [0] * m
    for i in range(m):
        a = LI()
        A.append(a[1:])
        if a[0] == 1:
            cnt[a[1]] += 1
            ans[i] = a[1]

    if max(cnt) > (m + 1) // 2:
        print('NO')
        continue
    for i in range(m):
        if len(A[i]) == 1:
            continue
        ans[i] = A[i][0]
        for x in A[i]:
            if cnt[x] <= cnt[ans[i]]:
                ans[i] = x
        cnt[ans[i]] += 1
    print('YES')
    print(*ans)
