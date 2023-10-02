# _*_ coding: utf-8 _*_
# @Time : 2023/01/30 7:26 PM 
# @Author : yefe
# @File : 2552_countQuadruplets

from typing import List
from datetime import datetime, timedelta

date_str = '20190102'
N = 1

date_obj = datetime.strptime(date_str, '%Y%m%d')
target_date_obj = date_obj+timedelta(N)
print(target_date_obj.strftime('%Y%m%d'))


# class Solution:
#     def countQuadruplets(self, nums: List[int]) -> int:
#         n = len(nums)
#         great = [0]*n
#         great[-1] = [0]*(n+1)
