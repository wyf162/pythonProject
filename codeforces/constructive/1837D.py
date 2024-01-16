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
    s = input()
    if s.count('(') != s.count(')'):
        print(-1)
        continue

    c2 = []
    stk = []
    for i in range(n-1, -1, -1):
        if s[i] == ')':
            if stk and stk[-1][0] == '(':
                c2.append(stk[-1][1])
                c2.append(i)
                stk.pop()
            else:
                stk.append((s[i], i))
        else:
            stk.append((s[i], i))

    c1 = []
    stk = []
    for i in range(n):
        if s[i] == ')':
            if stk and stk[-1][0] == '(':
                c1.append(stk[-1][1])
                c1.append(i)
                stk.pop()
            else:
                stk.append((s[i], i))
        else:
            stk.append((s[i], i))
    if len(c1) == n or len(c1) == 0 or len(c2) == n or len(c2) == 0:
        print(1)
        print(*[1 for _ in range(n)])
    else:
        print(2)
        nums = [2] * n
        for i in c1:
            nums[i] = 1
        print(*nums)
