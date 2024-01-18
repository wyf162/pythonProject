import sys

# sys.stdin = open('./../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    ans = 0
    ss = input().split('#')
    for s in ss:
        if s.count('.') == 1:
            ans += 1
        elif s.count('.') == 2:
            ans += 2
        elif s.count('.') > 2:
            ans = 2
            break
    print(ans)
