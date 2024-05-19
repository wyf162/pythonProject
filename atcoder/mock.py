import random
import sys

sys.stdout = open('./input.txt', 'w')

E5 = 10 ** 5
E9 = 10 ** 9
E18 = 10 ** 18

tcn = 100
print(tcn)
for _tcn_ in range(tcn):
    n = 6
    print(n)
    nums = [random.randint(1, 10) for _ in range(n)]
    print(*nums)
