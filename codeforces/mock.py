import random
import sys
from string import ascii_lowercase

sys.stdout = open('./input.txt', 'w')


def generate_random_string(length):
    return ''.join(random.choice(ascii_lowercase[:10]) for _ in range(length))


def make_graph(n):
    vertexes = list(range(1, n + 1))
    w = 1
    edges = []
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            edges.append((i, j, w))
    m = len(edges)
    for state in range((1 << m) - 10000, 1 << m):
        if bin(state).count('1') < n:
            continue
        print(n, bin(state).count('1'))
        for j in range(m):
            if state >> j & 1:
                print(*edges[j])


E5 = 10 ** 5
E9 = 10 ** 9
E18 = 10 ** 18

tcn = 1
# print(tcn)
for _tcn_ in range(tcn):
    n = 5000
    nums = [random.randint(1, 9) for i in range(n)]
    print(n)
    print(''.join(str(x) for x in nums))

    # n, q = 10, 10
    # cur = 0
    # print(n, q)
    # for i in range(n):
    #     if i % 6 < 3:
    #         cur += 1
    #         print(1, random.randint(1, 100))
    #     else:
    #         x = random.randint(1, 100)
    #         print(2, x)
    #         cur *= (x + 1)
    # queries = [random.randint(1, cur) for _ in range(q)]
    # print(*queries)
    # print(cur < 10 ** 18)
