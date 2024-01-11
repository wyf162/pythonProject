import sys

sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    s = input()
    n = len(s)
    zero = s.count('0')
    one = s.count('1')
    i, j = 0, n - 1
    count_one = 0
    count_zero = 0
    # [l, r]
    # ans = min(r - l + 1 - 2 * count_one)
    # print(ans)

