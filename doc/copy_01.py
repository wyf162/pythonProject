import sys, os, io

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


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


if __name__ == '__main__':
    x = 959345256
    ft = len(divisors(x))
    print(divisors(x))
    print(ft)
