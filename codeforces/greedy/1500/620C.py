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
a = LI()

ans = []
s = set()
pre = 1
for i in range(n):
    if a[i] in s:
        ans.append([pre, i + 1])
        pre = i + 2
        s = set()
    else:
        s.add(a[i])


if ans:
    ans[-1][1] = n
    print(len(ans))
    for i in range(len(ans)):
        print(*ans[i])
else:
    print(-1)
