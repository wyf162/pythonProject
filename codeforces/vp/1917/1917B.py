import sys

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())


def idx(c):
    return ord(c) - ord('a')


tcn = I()
for _tcn_ in range(tcn):
    n = I()
    s = list(input())
    state = [0] * (n + 1)
    ans = 0
    for i in range(1, n + 1):
        x = idx(s[i - 1])
        state[i] = state[i - 1] | (1 << x)
        ans += bin(state[i]).count('1')
    print(ans)
