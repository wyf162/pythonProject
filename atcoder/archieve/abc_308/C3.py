from functools import cmp_to_key


def cmp(a, b):
    _, x1, y1 = a
    _, x2, y2 = b
    if x1 * (x2 + y2) == x2 * (x1 + y1): return 0
    return 1 if x1 * (x2 + y2) < x2 * (x1 + y1) else -1


N = int(input())
A = [[i] + list(map(int, input().split())) for i in range(N)]
B = sorted(A, key=cmp_to_key(cmp))
print(*[e[0] + 1 for e in B])
