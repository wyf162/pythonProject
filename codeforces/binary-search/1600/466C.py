import bisect
import sys

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n = I()
a = LI()
s = sum(a)
if s % 3:
    print(0)
    exit(0)

s = s // 3
pre = 0
one, two = [], []
for i in range(n):
    pre += a[i]
    if pre == s:
        one.append(i)
    if pre == s * 2:
        two.append(i)

if two and two[-1] == n - 1:
    two.pop()
ans = 0
for x in one:
    i = bisect.bisect_right(two, x)
    ans += len(two) - i
print(ans)
