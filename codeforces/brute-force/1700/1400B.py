import sys

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))
mod = 998244353

tcn = I()
for _tcn_ in range(tcn):
    p, f = MI()
    cnt_s, cnt_w = MI()
    s, w = MI()
    if s > w:
        cnt_s, cnt_w = cnt_w, cnt_s
        s, w = w, s
    # sword < war axes
    # first select sword
    ans = 0
    for i in range(cnt_s+1):
        if p < i * s:
            break
        a = i
        b = min((p - a * s) // w, cnt_w)
        last_s = cnt_s - a
        last_w = cnt_w - b

        c = min(f // s, last_s)
        last_f = f - c * s
        d = min(last_f // w, last_w)
        ans = max(ans, a + b + c + d)
    print(ans)
