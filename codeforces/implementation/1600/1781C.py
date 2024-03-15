import sys

sys.stdin = open('../../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LI = lambda: list(MI())
LGMI = lambda: list(GMI())
mod = 1000000007
mod2 = 998244353

idx = lambda x: ord(x) - ord('a')

tcn = I()
for _tcn_ in range(tcn):
    n = I()
    s = input()
    t = ['*'] * n
    a = [[x, 0] for x in 'abcdefghijklmnopqrstuvwxyz']
    for c in s:
        # print(idx(c))
        a[idx(c)][1] += 1
    a.sort(key=lambda x: -x[1])
    ans = n
    for i in range(1, 27, 1):
        if n % i:
            continue
        k = n // i
        rst = 0
        for j in range(26):
            if j < i:
                if a[j][1] > k:
                    rst += a[j][1] - k
            else:
                rst += a[j][1]

        if rst < ans:
            ans = rst
            cnt = [0] * 26
            t = ['*'] * n
            for j in range(i):
                for i2 in range(n):
                    if s[i2] == a[j][0]:
                        if cnt[j] < k:
                            t[i2] = a[j][0]
                            cnt[j] += 1
            for j in range(i):
                for i2 in range(n):
                    if cnt[j] < k and t[i2] == '*':
                        t[i2] = a[j][0]
                        cnt[j] += 1

    print(ans)
    # print(t)
    print(''.join(t))
