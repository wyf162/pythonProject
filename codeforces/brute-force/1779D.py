import sys
from collections import Counter, defaultdict

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = int(input())
for _tcn_ in range(tcn):
    n = I()
    a = LI()
    b = LI()
    a.insert(0, 0)
    b.insert(0, 0)
    m = I()
    razor = LI()

    d = [0] * (4 * n + 4)


    def build(s, t, p):
        if s == t:
            d[p] = b[s]
            return
        m = s + ((t - s) >> 1)
        build(s, m, p * 2)
        build(m + 1, t, p * 2 + 1)
        d[p] = max(d[p * 2], d[(p * 2) + 1])


    def get_max(l, r, s, t, p):
        if l <= s and t <= r:
            return d[p]
        m = s + ((t - s) >> 1)
        mx = 0
        if l <= m:
            mx = max(mx, get_max(l, r, s, m, p * 2))
        if r > m:
            mx = max(mx, get_max(l, r, m + 1, t, p * 2 + 1))
        return mx


    build(1, n, 1)

    hst = Counter()
    ans = None
    stk = []
    for i in range(1, n + 1):
        if b[i] > a[i]:
            ans = False
            break
        elif b[i] < a[i]:
            if b[i] not in hst:
                hst[b[i]] = [i]
            else:
                l = hst[b[i]][-1]
                r = i
                mx = get_max(l, r, 1, n, 1)
                if mx > b[i]:
                    hst[b[i]].append(i)
    if ans is False:
        print('No')
        continue

    ks = sorted(hst.keys(), reverse=True)
    cnt = Counter(razor)
    for i, k in enumerate(ks):
        if len(hst[k]) > cnt[k]:
            ans = False
            break
    if ans is False:
        print('No')
    else:
        print('Yes')
