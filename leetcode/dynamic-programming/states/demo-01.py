# _*_ coding: utf-8 _*_
# @Time : 2022/08/28 12:46 AM 
# @Author : yefe
# @File : demo-00


def subset(mask):
    rets = [mask]
    x = mask
    while x > 0:
        x = (x - 1) & mask
        rets.append(x)
    for ret in rets:
        print(format(ret, '0=3b'))


if __name__ == '__main__':
    subset(6)
