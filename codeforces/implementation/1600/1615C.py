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
    s1 = input()
    s2 = input()
    if s1 == s2:
        print(0)
        continue
    if s1.count('1') == 0:
        print(-1)
        continue

    x00 = x01 = x11 = x10 = 0
    for i in range(n):
        if s1[i] == '0' and s2[i] == '0':
            x00 += 1
        if s1[i] == '0' and s2[i] == '1':
            x01 += 1
        if s1[i] == '1' and s2[i] == '1':
            x11 += 1
        if s1[i] == '1' and s2[i] == '0':
            x10 += 1

    ans1 = ans2 = 1 << 30
    if x11 == x00 + 1:
        ans1 = x11 + x00
    if x10 == x01:
        ans2 = x10 + x01
    ans = min(ans1, ans2)
    if ans == 1 << 30:
        print(-1)
    else:
        print(ans)
