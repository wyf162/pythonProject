# _*_ coding: utf-8 _*_
# @Time : 2022/2/19 下午3:19 
# @Author : wangyefei
# @File : bit_operation.py


def test_state():
    x = int('10110100', 2)
    print(x)
    for i in range(0, 8):
        s = x & (1 << i)
        print(f"bit {i} state {bin(s)}")
    for i in range(8):
        print(f"bit {i} state {bin(x)}")
        s = x | (1 << i)
        print(f"bit {i} state {bin(s)}")
        print(f"bit {i} state {bin(s ^ x)}")


def test_grey_code():
    n = 8
    binary_list = [i for i in range(n)]
    print([" ".join([format(x, '0=3b') for x in binary_list])])
    grey_list = list()
    for i in range(n):
        grey_list.append((i>>1)^i)
    print([" ".join([format(x, '0=3b') for x in grey_list])])


if __name__ == '__main__':
    test_grey_code()
    # test_state()
