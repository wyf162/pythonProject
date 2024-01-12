import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../input.txt', 'r')
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
    a, b = MI()
    B = 30
    rst = b - a
    for ax in range(a, b + 1, 1):
        bx = 0
        for i in range(B, -1, -1):
            if ax >> i & 1 == 1 and b >> i & 1 == 0:
                bx |= (1 << i)
                break
            else:
                bx |= (b >> i & 1) << i
                # break
        op = ax - a + (bx | ax) - b + int(bx | ax != ax)
        rst = min(op, rst)
    print(rst)
