import random
import sys

sys.stdout = open('./input.txt', 'w')
tcn = 1000
print(tcn)
for _tcn_ in range(tcn):
    print(random.randint(1, 100), random.randint(1, 100))
    # n = 100
    # m = 100
    # print(n, m)
    # a = [random.randint(1, 30) for _ in range(n)]
    # print(*a)
    # for i in range(m):
    #     print(random.randint(1, 2), random.randint(1, 10))
