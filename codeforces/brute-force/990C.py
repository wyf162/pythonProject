import sys
from collections import Counter

input = lambda: sys.stdin.readline().rstrip('\r\n')
sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

n = I()
hst = Counter()
ans = 0
for i in range(n):
    s = input()
    stk = []
    for c in s:
        if c == '(':
            stk.append(c)
        else:
            if stk and stk[-1] == '(':
                stk.pop()
            else:
                stk.append(c)
    if '(' in stk and ')' in stk:
        continue
    s = ''.join(stk)
    hst[s] += 1
    if '(' in s:
        t = ')' * len(s)
        ans += hst[t]
    elif ')' in s:
        t = '(' * len(s)
        ans += hst[t]

ans += hst[''] * hst['']
print(ans)
