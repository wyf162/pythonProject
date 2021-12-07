# -*- coding : utf-8 -*-
# @Time: 2021/12/7 22:12
# @Author: yefei.wang
# @File: compare-dict-class.py
import sys


class People(object):
    __slots__ = ['name', 'sex', 'age', 'location']

    def __init__(self, name, sex, age, location):
        self.name = name
        self.sex = sex
        self.age = age
        self.location = location


if __name__ == "__main__":
    p = People("Guido", 'man', 12, 'Shanghai')
    d = {"name": "Guido", "sex": 'man', "age": 12, "location": "Shanghai"}
    print(sys.getsizeof(p))
    print(sys.getsizeof(d))
