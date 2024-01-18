import sys

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 10 ** 9 + 7

n = I()
a = LI()
a.sort()

s = sum(a)
x = s // n
y = s % n
b = [x] * (n - y) + [x + 1] * y

rst = 0
for i in range(n):
    if a[i] < b[i]:
        rst += b[i] - a[i]
print(rst)
