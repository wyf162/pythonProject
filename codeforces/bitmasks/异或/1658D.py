import sys

input = lambda: sys.stdin.readline().rstrip('\r\n')
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
    l, r = MI()
    a = LI()
    cnt = [[0] * 2 for _ in range(32)]
    for x in a:
        for i in range(31):
            cnt[i][x & 1] += 1
            x >>= 1
    ans = 0
    for i in range(31):
        if cnt[i][0] < cnt[i][1]:
            ans |= (1 << i)
    print(ans)
