# _*_ coding: utf-8 _*_
# @Time : 2022/05/23 10:35 PM 
# @Author : yefe
# @File : 731_my_calendar2

class Node:
    def __init__(self, ls=0, rs=0, add=0, max=0):
        self.ls = ls
        self.rs = rs
        self.add = add
        self.max = max




class MyCalendar:
    def __init__(self):
        self.n = int(1e9)
        self.m = 120010
        self.cnt = 1
        self.tr = [Node()]*self.m
    def book(self, start: int, end: int) -> bool:
        pass

if __name__ == '__main__':
    my_calendar = MyCalendar()
    ret = my_calendar.book(10, 20)
    print(ret)
    ret = my_calendar.book(15, 25)
    print(ret)
    ret = my_calendar.book(20, 30)
    print(ret)