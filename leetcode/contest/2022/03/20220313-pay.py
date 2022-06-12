# _*_ coding: utf-8 _*_
# @Time : 2022/3/13 下午5:26 
# @Author : wangyefei
# @File : 20220313-pay.py
import collections
import heapq
from typing import List


class Solution:
    def isPalindrome(self, nums) -> bool:
        # nums = []
        # while head:
        #     nums.append(head.val)
        #     head=head.next
        i = 0
        j = len(nums) - 1
        ret = True
        cnt = 0
        while i < j:
            if nums[i] == nums[j]:
                i += 1
                j -= 1
            else:
                if nums[i] == nums[j - 1]:
                    i += 1
                    j -= 2
                    cnt += 1
                elif nums[i + 1] == nums[j]:
                    i += 2
                    j -= 1
                    cnt += 1
                else:
                    return False
        print(ret, cnt)
        return ret if cnt < 2 else False

    def maxInvestment2(self, product: List[int], limit: int) -> int:
        product = [-1 * price for price in product]
        heapq.heapify(product)
        res = 0
        while len(product) > 0 and limit > 0:
            price = heapq.heappop(product)
            res -= price
            limit -= 1
            price += 1
            if price < 0:
                heapq.heappush(product, price)
        res = res%1000000007
        return res

    def maxInvestment(self, product: List[int], limit: int) -> int:
        product.sort(reverse=True)



class DiscountSystem:

    def __init__(self):
        self.activities = dict()
        self.user_activity_record = collections.defaultdict(dict)

    def addActivity(self, actId: int, priceLimit: int, discount: int, number: int, userLimit: int) -> None:
        self.activities[actId] = {'price_limit': priceLimit,
                                  'discount': discount,
                                  'number': number,
                                  'user_limit': userLimit,
                                  'is_removed': False}

    def removeActivity(self, actId: int) -> None:
        self.activities[actId]['is_removed'] = True

    def consume(self, userId: int, cost: int) -> int:
        cur_discount = None
        tmp_act_id = None
        for act_id, act_info in self.activities.items():
            price_limit = act_info.get('price_limit')
            discount = act_info.get('discount')
            number = act_info.get('number')
            user_limit = act_info.get('user_limit')
            is_removed = act_info.get('is_removed')
            if is_removed or number <= 0 or self.user_activity_record.get(userId, dict()).get(act_id, 0) >= user_limit:
                continue
            if cost < price_limit:
                continue
            if tmp_act_id is None:
                cur_discount = discount
                tmp_act_id = act_id
            elif discount > cur_discount:
                cur_discount = discount
                tmp_act_id = act_id
        if cur_discount is None:
            return cost
        else:
            self.activities[tmp_act_id]['number'] -= 1
            self.user_activity_record[userId][tmp_act_id] = self.user_activity_record[userId].get(tmp_act_id, 0) + 1
            return cost - cur_discount


if __name__ == '__main__':
    obj = DiscountSystem()
    obj.addActivity(1, 10, 6, 3, 2)
    obj.addActivity(2, 15, 8, 8, 2)
    ret = obj.consume(101, 13)
    print(ret)
    obj.removeActivity(2)
    ret = obj.consume(101, 17)
    print(ret)
    ret = obj.consume(101, 11)
    print(ret)

    # sol = Solution()
    # nums = [7,7,1,5,5,1,7,3]
    # ret = sol.isPalindrome(nums)
    # print(ret)
