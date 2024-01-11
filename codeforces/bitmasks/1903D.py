import copy
import sys

sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

n, q = MI()
A = LI()
qs = [I() for _ in range(q)]

B = 60

for q in qs:
    ans = 0
    a = copy.deepcopy(A)
    for b in range(B, -1, -1):
        t = 0
        c = dict()
        for i in range(n):
            if (a[i] >> b) & 1:
                continue
            else:
                v = (a[i] | (1 << b)) & ~((1 << b) - 1)
                t += v - a[i]
                c[i] = v
        if t <= q:
            q -= t
            ans |= (1 << b)
            for i, v in c.items():
                a[i] = v
    print(ans)
