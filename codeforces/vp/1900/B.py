import sys

# sys.stdin = open('./../../input.txt', 'r')
# sys.stdout = open('./../../output.txt', 'w')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))


def check(x, y, z):
    if y % 2 == z % 2:
        # if abs(y - z) <= 2 * x:
        return 1
    return 0


tcn = I()
for _tcn_ in range(tcn):
    a, b, c = MI()
    ans = [0, 0, 0]
    ans[0] = check(a, b, c)
    ans[1] = check(b, a, c)
    ans[2] = check(c, a, b)
    print(*ans)
