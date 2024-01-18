import sys

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 10 ** 9 + 7

n = I()
s = input()
op = 0
while len(s) > 1:
    t = ''
    for i in range(len(s) - 1):
        t += s[i] * int(s[i + 1])
    print(t)
    s = t
    op += 1
print(op)
