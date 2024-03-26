# sys.stdin = open('./../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(map(int, input().split()))
mod = 10 ** 9 + 7

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    b = LI()
    # bl + bm + br - r + l
    # bl + l, bm, br - r
    left = []
    for i in range(n):
        if not left or left[-1] < b[i] + i:
            left.append(b[i] + i)
        else:
            left.append(left[-1])
    right = []
    for i in range(n - 1, -1, -1):
        if not right or right[-1] < b[i] - i:
            right.append(b[i] - i)
        else:
            right.append(right[-1])

    rst = 0
    for m in range(1, n - 1):
        rst = max(rst, left[m - 1] + b[m] + right[n - 2 - m])
    print(rst)
