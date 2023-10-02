# _*_ coding: utf-8 _*_
# @Time : 2022/05/23 10:51 PM 
# @Author : yefe
# @File : 732_my_calendar
from sortedcontainers import SortedDict


class MyCalendarThree(object):

    def __init__(self):
        self.delta = SortedDict()

    def book(self, start, end):
        if start not in self.delta:
            self.delta[start]=0
        if end not in self.delta:
            self.delta[end]=0
        self.delta[start] += 1
        self.delta[end] -= 1

        active = ans = 0
        for x in self.delta:
            active += self.delta[x]
            if active > ans: ans = active

        return ans


if __name__ == '__main__':
    my_calendar = MyCalendarThree()
    ret = my_calendar.book(10, 20)
    print(ret)
    ret = my_calendar.book(15, 25)
    print(ret)
    ret = my_calendar.book(18, 30)
    print(ret)