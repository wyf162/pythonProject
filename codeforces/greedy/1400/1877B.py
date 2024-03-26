# sys.stdin = open('./../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = int(input())

for _tcn_ in range(tcn):
    n, p = MI()
    a = LI()
    b = LI()
    c = [[count, cost] for count, cost in zip(a, b)]
    c.sort(key=lambda x: x[1])
    tot = 0
    tot += p
    store = 1
    last = n-1
    for i in range(n):
        if store > 0:
            store -= 1
        else:
            tot += p
            last -= 1
        if c[i][1] < p:
            store += c[i][0]
            if c[i][0] < last:
                tot += c[i][0] * c[i][1]
                last -= c[i][0]
            else:
                tot += c[i][1] * last
                last_count = 0
                break
    print(tot)
