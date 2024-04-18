import datetime
from operator import gt
from functools import partial


def gcd(m, n):
    while n != 0:
        m, n = n, m % n

    return m


if __name__ == '__main__':
    a = 10
    b = 1
    ret = gt(a, b)
    gt2 = partial(gt, a)
    ret2 = gt2(b)
    print(ret2)
