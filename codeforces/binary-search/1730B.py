import sys

sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    a = LI()
    b = LI()


    def check(y):
        L, R = -1e9, 1e9
        for x, t in zip(a, b):
            if y < t:
                return False, None
            d = y - t
            L = max(L, x - d)
            R = min(R, x + d)
            if L > R:
                return False, None
        return True, (L + R) / 2


    l, r = 0, 1e9
    ans = 1e9
    while l <= r:
        m = l + (r - l) / 2
        isvalid, x0 = check(m)
        if isvalid:
            ans = x0
            r = m - 1e-6
        else:
            l = m + 1e-6

    print(ans)
