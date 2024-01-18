from sortedcontainers import *

n, k, q = map(int, input().split())
f = SortedList([0] * k)
g = SortedList([0] * (n - k))
a = [0] * n
s = 0
for _ in range(q):
    x, y = map(int, input().split())
    x -= 1
    if a[x] < f[0]:
        g.discard(a[x])
    else:
        f.discard(a[x])
        s -= a[x]
        if g:
            f.add(g.pop())
            s += f[0]
    a[x] = y
    if len(f) == k and a[x] < f[0]:
        g.add(a[x])
    elif len(f) == k:
        s += a[x] - f[0]
        g.add(f[0])
        f.discard(f[0])
        f.add(a[x])
    else:
        s += a[x]
        f.add(a[x])
    print(s)
