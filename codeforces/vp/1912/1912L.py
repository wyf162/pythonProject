import sys

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())

n = I()
s = input()

x = s.count('L')
y = s.count('O')
x1, y1 = 0, 0
for i in range(n):
    if s[i] == 'L':
        x1 += 1
    elif s[i] == 'O':
        y1 += 1

    x2 = x - x1
    y2 = y - y1
    if x1 != x2 and y1 != y2 and x2 + y2 > 0:
        exit(print(i + 1))

exit(print(-1))
