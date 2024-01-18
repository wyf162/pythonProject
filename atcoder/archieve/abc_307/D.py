import sys

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

n = I()
s = input()
stk = []
left = []

for i in range(n):
    if s[i] == '(':
        left.append(len(stk))
        stk.append(s[i])
    elif s[i] == ')':
        if left:
            j = left.pop()
            while len(stk) > j:
                stk.pop()
        else:
            stk.append(s[i])
    else:
        stk.append(s[i])

print(''.join(stk))
