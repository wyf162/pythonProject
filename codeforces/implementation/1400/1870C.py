import sys
# sys.stdin = open('../input.txt', 'r')


def int_get(): return int(input())


def ints_get(): return map(int, input().strip().split())


def int_list_get(): return list(map(int, sys.stdin.readline().strip().split()))


def solve(n, k, a):
    l = [n + 1] * (k + 1)
    r = [0] * (k + 1)
    mx = 0
    for i in range(n):
        mx = max(mx, a[i])
        l[a[i]] = min(l[a[i]], i)
        r[a[i]] = max(r[a[i]], i)
    pre = mx
    for i in range(mx - 1, 0, -1):
        if l[i] == n + 1:
            continue
        l[i] = min(l[pre], l[i])
        r[i] = max(r[pre], r[i])
        pre = i
    for i in range(1, k + 1, 1):
        if l[i] == n + 1:
            print(0, end=' ')
        else:
            print(2 * (r[i] - l[i] + 1), end=' ')
    print()


def main():
    tcn = int_get()
    for _ in range(tcn):
        n, k = ints_get()
        a = int_list_get()
        solve(n, k, a)


if __name__ == '__main__':
    main()
