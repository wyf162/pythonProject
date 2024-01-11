import sys
from string import ascii_lowercase

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))
YN = lambda x: print('YES' if x else 'NO')
Yn = lambda x: print('Yes' if x else 'No')

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    ss = [input() for _ in range(n)]
    ans = False
    hst = set()
    for s in ss:
        if len(s) == 3:
            if s[0] == s[2]:
                ans = True
                break
            elif s[2]+s[1] in hst:
                ans = True
                break
            elif s[2]+s[1]+s[0] in hst:
                ans = True
                break
        elif len(s) == 2:
            if s[0] == s[1]:
                ans = True
                break
            elif s[1]+s[0] in hst:
                ans = True
                break
            for c in ascii_lowercase:
                if s[1]+s[0]+c in hst:
                    ans = True
                    break
            if ans:
                break
        elif len(s) == 1:
            ans = True
            break
        hst.add(s)
    YN(ans)
