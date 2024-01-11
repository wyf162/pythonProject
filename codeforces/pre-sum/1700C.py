import sys

# sys.stdin = open('./../input.txt', 'r')
# sys.stdout = open('./../output.txt', 'w')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    a = LI()
    # op1 d1 <- d1 -1, di <- di + 1
    # op2 di <- di - 1
    # op3 d1 <- d1 + 1
    d = [0] * n
    d[0] = a[0]
    for i in range(1, n):
        d[i] = a[i] - a[i - 1]

    ans, tmp = 0, 0
    for i in range(1, n):
        if d[i] < 0:
            tmp += -d[i]
        if d[i] > 0:
            ans += d[i]
    ans += tmp
    if tmp > d[0]:
        ans += tmp - d[0]
    else:
        ans += d[0] - tmp
    print(ans)
