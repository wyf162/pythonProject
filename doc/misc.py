import sys, os, io
from collections import defaultdict, Counter
from random import getrandbits

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

RANDOM = getrandbits(32)


class Wrapper(int):
    def __init__(self, x):
        int.__init__(x)

    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ RANDOM


def divisors(M):
    d = []
    i = 1
    while M >= i ** 2:
        if M % i == 0:
            d.append(i)
            if i ** 2 != M:
                d.append(M // i)
        i = i + 1
    return d


# 据说defaultdict(int)比Counter() 快
cnt = Counter()
hst = defaultdict(int)

if __name__ == '__main__':
    print(hst[0])
    # x = 959345256
    # ft = len(divisors(x))
    # print(divisors(x))
    # print(ft)
