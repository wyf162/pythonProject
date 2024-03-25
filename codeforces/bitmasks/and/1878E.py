import sys

# sys.stdin = open('../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

# Iva and Pav

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    a = LI()
    qn = I()
    queries = [LI() for _ in range(qn)]

    B = 32
    pres = [[0] for _ in range(B)]
    for i in range(n):
        for b in range(B):
            pres[b].append(pres[b][-1] + int(a[i] >> b & 1))

    for query in queries:
        L, k = query
        l, r = L - 1, n - 1
        if k > a[l]:
            print('-1', end=' ')
            continue

        ans = l
        while l <= r:
            m = (l + r) >> 1
            v = 0
            for b in range(B):
                if pres[b][m + 1] - pres[b][L - 1] == m - L + 2:
                    v |= 1 << b
            if v >= k:
                ans = m
                l = m + 1
            else:
                r = m - 1
        print(ans + 1, end=' ')
    print()
