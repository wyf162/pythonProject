import sys

sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

tcn = I()
for _tcn_ in range(tcn):
    x = I()
    s = bin(x)[2:]
    s1 = ''
    s2 = ''
    i = 0
    while i < len(s):
        if s[i] == '1':
            if i + 1 < len(s) and s[i + 1] == '0':
                s1 += '11'
                s2 += '01'
                i += 2
            else:
                s1 = ''
                s2 = ''
                break
        else:
            s1 += '0'
            s2 += '0'
            i += 1
    if s1:
        x1, x2 = int(s1, 2), int(s2, 2)
        print(x1, x2)
        # print(x1 ^ x2, (x1 + x2))
    else:
        print(-1)
