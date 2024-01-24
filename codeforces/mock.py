import random
import sys

sys.stdout = open('./input.txt', 'w')
tcn = 100
print(tcn)
for _tcn_ in range(tcn):
    n = 10
    print(n, n)
    a = [random.randint(1, 3) for _ in range(n)]
    b = [random.randint(1, 3) for _ in range(n)]
    c = [random.randint(1, 3) for _ in range(n)]
    b[-1] = c[-1]
    print(*a)
    print(*b)
    print(*c)
