# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = int(input())

for _tcn_ in range(tcn):
    n = I()
    a = LI()
    ans = 0 - sum(a)
    print(ans)
