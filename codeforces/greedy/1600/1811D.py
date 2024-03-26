# sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())

fib = [1, 1]
for _ in range(44):
    fib.append(fib[-1] + fib[-2])
# print(fib)

tcn = I()
for _tcn_ in range(tcn):
    n, x, y = MI()

    l, r = 1, fib[n + 1]
    u, d = 1, fib[n]
    success = 1
    for i in range(n, 1, -1):
        if r - l + 1 > d - u + 1:
            if y > l + fib[i] - 1:
                l += fib[i]
            elif y < r - fib[i] + 1:
                r -= fib[i]
            else:
                success = 0
                break
        else:
            if x > u + fib[i] - 1:
                u += fib[i]
            elif x < d - fib[i] + 1:
                d -= fib[i]
            else:
                success = 0
                break
    if success:
        print('Yes')
    else:
        print('No')
