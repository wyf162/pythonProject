# _*_ coding: utf-8 _*_
# @Time : 2023/01/08 1:32 PM 
# @Author : yefe
# @File : 2526_DataStream
class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.pre = -1
        self.cur = -1

    def consec(self, num: int) -> bool:
        self.cur += 1
        if num != self.value:
            self.pre = self.cur
        return self.cur - self.pre >= self.k
