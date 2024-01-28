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
    a, b, x = MI()
    if a < b:
        a, b = b, a

    ans = False
    while True:
        if a < x:
            break
        if b == 0:
            if a == x or b == x:
                ans = True
            break
        if a == x or b == x or (a - x) % b == 0:
            ans = True
            break
        a, b = b, a % b

    YN(ans)
