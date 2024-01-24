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
    n = I()
    s = list(input())
    one = s.count('1')
    zero = s.count('0')
    if s[0] != '1' or s[-1] != '1' or one % 2  or zero % 2:
        print('NO')
        continue

    a, b = 0, 0
    s1, s2 = [], []
    ans = True
    c = 0
    for i in range(n):
        if s[i] == '1':
            if c * 2 < one:
                s1.append('(')
                s2.append('(')
                a += 1
                b += 1
                c += 1
            else:
                s1.append(')')
                s2.append(')')
                a -= 1
                b -= 1
        else:
            if a >= b:
                s1.append(')')
                s2.append('(')
                a -= 1
                b += 1
            else:
                s1.append('(')
                s2.append(')')
                a += 1
                b -= 1
    print('YES')
    print(''.join(s1))
    print(''.join(s2))
