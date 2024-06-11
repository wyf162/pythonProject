import random
import sys

sys.stdout = open('./input.txt', 'w')

E5 = 10 ** 5
E9 = 10 ** 9
E18 = 10 ** 18

tcn = 1
# print(tcn)
for _tcn_ in range(tcn):
    # n = 2000
    # print(n)
    # for i in range(n):
    #     print(i, n - i - 1)
    n = 2000
    print(n)
    for i in range(1, n + 1):
        print(i // 2, 0)
