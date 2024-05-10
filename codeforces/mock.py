import random
import sys

sys.stdout = open('./input.txt', 'w')
tcn = 1
for _tcn_ in range(tcn):
    n = 2
    print(2)
    for _ in range(n):
        n1 = 100
        nums = [n1] + list(range(1, n1+1, 1))
        print(*nums)
    m = 2500
    print(m)
    for i in range(100, 50, -1):
        for j in range(100, 50, -1):
            print(i, j)
    # print(*a)
    # for i in range(m):
    #     print(random.randint(1, 2), random.randint(1, 10))
