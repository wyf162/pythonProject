import sys

# sys.stdin = open('./../input.txt', 'r')
I = lambda: int(input())
MI = lambda: map(int, input().split())
LI = lambda: list(map(int, input().split()))


def max_n_digit(n):
    return int('9' * n)


def min_n_digit(n):
    return int('1' + '0' * (n - 1))


tcn = I()
for _tcn_ in range(tcn):
    A, B, C, k = MI()
    if C > max(A, B) + 1:
        print(-1)
        continue
    mi_a, mx_a = min_n_digit(A), max_n_digit(A)
    mi_b, mx_b = min_n_digit(B), max_n_digit(B)
    mi_c, mx_c = min_n_digit(C), max_n_digit(C)

    for a in range(mi_a, mx_a+1):
        cnt = min(mx_b, mx_c - a) - max(mi_b, mi_c - a) + 1
        if cnt < 0:
            continue
        if k > cnt:
            k -= cnt
            continue
        else:
            b = max(mi_b, mi_c - a) + k - 1
            print(f"{a} + {b} = {a + b}")
            break
    else:
        print(-1)
