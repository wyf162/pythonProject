import sys

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

n, m = MI()
s = input()

y = m
x = 0
ans = 0
for i, c in enumerate(s):
    if c == '0':
        y = m
        x = 0

    elif c == '1':
        if y:
            y -= 1
        else:
            x -= 1

    elif c == '2':
        x -= 1
    ans = max(ans, abs(x))
print(ans)
