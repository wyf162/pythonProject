# sys.stdin = open('./../input.txt', 'r')
# sys.stdout = open('./../output.txt', 'w')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    s = input()
    ans = 0
    c = 1
    for i in range(1, n):
        if s[i] == s[i - 1]:
            ans += 1
            ans = min(ans, c)
        else:
            c += 1
    print((c + ans + 1) // 2)
