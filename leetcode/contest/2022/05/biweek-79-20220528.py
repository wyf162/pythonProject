# _*_ coding: utf-8 _*_
# @Time : 2022/05/28 10:29 PM 
# @Author : yefe
# @File : biweek-79-20220528
from collections import defaultdict
from typing import List


class Solution:
    def digitCount(self, num: str) -> bool:
        hst = defaultdict(int)
        n = len(num)
        for i in range(n):
            hst[num[i]] += 1
        for i in range(n):
            if hst[str(i)] == int(num[i]):
                continue
            else:
                return False
        return True

    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        hst = defaultdict(int)
        for message, sender in zip(messages, senders):
            hst[sender] += len(message.split(" "))

        ret = senders[0]
        cnt = hst[ret]
        for sender, count in hst.items():
            if count>cnt:
                ret = sender
                cnt = count
            elif count==cnt and sender>ret:
                ret = sender
        return ret

    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degrees = [0]*n
        for x, y in roads:
            degrees[x] += 1
            degrees[y] += 1

        degrees.sort()
        res = 0
        for i, degree in enumerate(degrees):
            res += (i+1)*degree
        return res





if __name__ == '__main__':
    sol = Solution()
    n = 5
    roads = [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]
    ret = sol.maximumImportance(n, roads)
    print(ret)


    # messages = ["Hello userTwooo", "Hi userThree", "Wonderful day Alice", "Nice day userThree"]
    # senders = ["Alice", "userTwo", "userThree", "Alice"]
    # ret = sol.largestWordCount(messages, senders)
    # print(ret)

    # num = '1210'
    # ret = sol.digitCount(num)
    # print(ret)
