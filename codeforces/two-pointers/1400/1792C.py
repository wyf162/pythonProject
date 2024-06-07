import sys

# sys.setrecursionlimit(10 ** 6)
# sys.stdin = open('./../input.txt', 'r')
# sys.stdout = open('./../output.txt', 'w')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))
tcn = I()
for _tcn_ in range(tcn):
    n = I()
    nums = LI()

    rst = 0
    i, l, r, s, e = 1, 1, n, 0, n - 1
    while True:
        if e - s < 1 or i > (n + 1) // 2:
            break

        while s < n:
            if nums[s] < i or nums[s] > n - i + 1:
                s += 1
            elif nums[s] == l:
                l += 1
                s += 1
            else:
                break

        while e < n:
            if nums[e] > n - i + 1 or nums[e] < i:
                e -= 1
            elif nums[e] == r:
                r -= 1
                e -= 1
            else:
                break
        rst += int(l < r)
        l = max(i + 1, l)
        r = min(n - i + 1, r)
        i = i + 1

    print(rst)
