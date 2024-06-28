import random
import sys
from string import ascii_lowercase

sys.stdout = open('./input.txt', 'w')


def generate_random_string(length):
    return ''.join(random.choice(ascii_lowercase[:10]) for _ in range(length))



E5 = 10 ** 5
E9 = 10 ** 9
E18 = 10 ** 18

tcn = 1000
print(tcn)
for _tcn_ in range(tcn):
    n = 100
    print(n)
    print(generate_random_string(n))
