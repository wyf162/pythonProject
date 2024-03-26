# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))

tcn = I()
for _tcn_ in range(tcn):
    s = input()
    k = I()
    if k == 0:
        print(s)
        continue

    n = len(s)
    stk = ['9']
    t = -1
    for i in range(k+1):
        if s[i] != '0' and s[i] < stk[0]:
            stk[0] = s[i]
            t = i
    k -= t
    for i in range(t+1, n):
        if i == t:
            continue
        while len(stk) > 1 and k > 0 and stk[-1] > s[i]:
            stk.pop()
            k -= 1
        stk.append(s[i])
    while k:
        stk.pop()
        k -= 1

    print(''.join(stk))
