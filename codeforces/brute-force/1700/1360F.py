import sys
from string import ascii_lowercase

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = int(input())

for _tcn_ in range(tcn):
    n, m = MI()
    ss = [input() for _ in range(n)]
    if n == 1:
        print(ss[0])
        continue


    def check(s1):
        for s in ss[1:]:
            diff = 0
            for i in range(m):
                diff += int(s[i] != s1[i])
            if diff > 1:
                return False
        return True


    rst = False

    for i in range(m):
        ans = list(ss[0])
        for c in ascii_lowercase:
            ans[i] = c
            rst = check(ans)
            if rst:
                print(''.join(ans))
                break

        if rst:
            break
    if not rst:
        print(-1)
