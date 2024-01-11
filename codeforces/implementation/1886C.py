import sys

sys.stdin = open('../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    s = input()
    pos = I()

    n = len(s)
    c = 0
    while pos > n:
        pos -= n
        c += 1
        n -= 1
    # print(c, pos)

    stk = []
    i = 0
    while i < len(s):
        while stk and stk[-1] > s[i]:
            stk.pop()
            c -= 1
            if c == 0:
                break
        stk.append(s[i])
        i += 1
        if c == 0:
            break
    if c == 0:
        while i < len(s):
            stk.append(s[i])
            i += 1
    else:
        while c:
            stk.pop()
            c -= 1
    ret = stk[pos - 1]
    print(ret, end='')
print()
