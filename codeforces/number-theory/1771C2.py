import sys

input = lambda: sys.stdin.readline().rstrip()

st = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37}


def is_prime64(n: int) -> bool:
    if n == 1: return False
    if n == 2: return True
    if n & 1 == 0: return False
    if n in st: return True
    d = (n - 1) >> 1
    while d & 1 == 0:
        d >>= 1
    for a in st:
        t = d
        y = pow(a, t, n)
        while t != n - 1 and y != 1 and y != n - 1:
            y = (y * y) % n
            t <<= 1
        if y != n - 1 and t & 1 == 0:
            return False
    return True


def get_primelist(MAX):
    is_prime = [1] * (MAX + 1)
    is_prime[0] = 0
    is_prime[1] = 0
    for i in range(2, int(MAX ** .5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i + i, MAX + 1, i):
            is_prime[j] = 0
    return [i for i, x in enumerate(is_prime) if x]


prime = get_primelist(31623)


#  -----------------------  #

def main():
    n = int(input())
    A = map(int, input().split())
    st = set()
    for a in A:
        if is_prime64(a):
            if a in st:
                return 'YES'
            st.add(a)
            continue
        for p in prime:
            if p * p > a:
                break
            if a % p == 0:
                if p in st:
                    return 'YES'
                st.add(p)
                a //= p
                while a % p == 0:
                    a //= p
        if a != 1:
            if a in st:
                return 'YES'
            st.add(a)
    return 'NO'


print('\n'.join(str(main()) for _ in range(int(input()))))
