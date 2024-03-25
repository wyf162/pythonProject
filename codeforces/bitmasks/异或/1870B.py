

def solve(n, m, a, b):
    y = 0
    for i in range(m):
        y |= b[i]

    mn, mx = 0, 0
    for i in range(n):
        mn ^= a[i]
        mx ^= (a[i] | y)
    if mn > mx:
        mx, mn = mn, mx
    print(mn, mx)


def main():
    tcn = int(input())
    for _ in range(tcn):
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        solve(n, m, a, b)


if __name__ == '__main__':
    main()
