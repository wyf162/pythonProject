import sys

# sys.stdin = open('./../input.txt', 'r')

I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

YN = lambda x: print('YES' if x else 'NO')
Yn = lambda x: print('Yes' if x else 'No')

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    mtx = [input() for i in range(n)]
    h = n // 2
    ans = 0
    for i in range(h):
        for j in range(h):
            x1, y1 = i, j
            x2, y2 = j, n - i - 1
            x3, y3 = n - i - 1, n - j - 1
            x4, y4 = n - j - 1, i
            abcd = [mtx[x1][y1], mtx[x2][y2], mtx[x3][y3], mtx[x4][y4]]
            # print(i, j, abcd)
            abcd.sort()
            for k in range(3):
                ans += ord(abcd[-1]) - ord(abcd[k])

    print(ans)
