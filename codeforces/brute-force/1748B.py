import sys

input = lambda: sys.stdin.readline().rstrip('\r\n')
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
    rst = 0
    n = I()
    s = [int(x) for x in input()]
    for i in range(n):
        cnt = [0] * 10
        mx = c = 0
        for j in range(i, min(n, i + 100)):
            cnt[s[j]] += 1
            c += int(cnt[s[j]] == 1)
            mx = max(cnt[s[j]], mx)
            rst += int(mx <= c)
    print(rst)
