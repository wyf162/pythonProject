import datetime


# import math
# from fractions import gcd

# year = 197
# month = 1
# day = 1
# d = datetime.datetime(year=year, month=month, day=day)
# print(d.timetuple().tm_wday)

def gcd(m, n):
    while n != 0:
        m, n = n, m % n

    return m


if __name__ == '__main__':
    print(gcd(4, 28))
