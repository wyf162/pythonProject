# _*_ coding: utf-8 _*_
# @Time : 2022/05/22 1:20 PM 
# @Author : yefe
# @File : 02

import datetime


def get_weekday(s):
    date_obj = datetime.datetime.strptime(s, "%Y%m%d")
    return date_obj.weekday()


if __name__ == "__main__":
    wd = get_weekday('20220522')
    print(wd)