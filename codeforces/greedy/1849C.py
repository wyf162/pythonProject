import sys

sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    n, m = MI()
    s = input()
    lf = [0] * n
    rg = [0] * n
    lf[0] = -1
    for i in range(n):
        if i > 0:
            lf[i] = lf[i - 1]
        if s[i] == '0':
            lf[i] = i
    rg[-1] = n
    for i in range(n - 1, -1, -1):
        if i + 1 < n:
            rg[i] = rg[i + 1]
        if s[i] == '1':
            rg[i] = i

    st = set()
    for _ in range(m):
        l, r = MI()
        ll, rr = rg[l - 1], lf[r - 1]
        if ll > rr:
            st.add((-1, -1))
        else:
            st.add((ll, rr))
    ans = len(st)
    print(ans)
