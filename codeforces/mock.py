import random
import sys

sys.stdout = open('./input.txt', 'w')


E5 = 10 ** 5
E9 = 10 ** 9
E18 = 10 ** 18

tcn = 1
# print(tcn)
for _tcn_ in range(tcn):
    n, m = 320, 312
    print(n, m)
    mtx = [[random.randint(1, E5) for _ in range(m)] for _ in range(n)]
    for i in range(n):
        print(*mtx[i])
