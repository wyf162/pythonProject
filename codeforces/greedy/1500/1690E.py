# sys.stdin = open('./../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = int(input())

for _tcn_ in range(tcn):
    n, k = MI()
    a = LI()

    count = [0] * k
    ans = 0
    for i in range(n):
        x, y = divmod(a[i], k)
        ans += x
        count[y] += 1

    l, r = 1, k - 1
    while l <= r:
        if l + r < k:
            l += 1
            continue

        while r >= l and l + r >= k:
            if r == l:
                ans += count[l] // 2
                count[l] = count[l] % 2
                count[r] = 0
                break
            elif count[l] < count[r]:
                ans += count[l]
                count[r] -= count[l]
                count[l] = 0
                break
            else:
                ans += count[r]
                count[l] -= count[r]
                count[r] = 0
                r -= 1
        l += 1
    print(ans)
