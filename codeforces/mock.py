import random
import sys

sys.stdout = open('./input.txt', 'w')

E5 = 10 ** 5
E9 = 10 ** 9
E18 = 10 ** 18

tcn = 1
print(tcn)
for _tcn_ in range(tcn):
    n = 3000
    print(n)
    nums = [10 for _ in range(n)]
    print(*nums)
    for i in range(n-1):
        print(i+1, i+2, 1)
