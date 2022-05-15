# _*_ coding: utf-8 _*_
# @Time : 2022/05/02 3:32 PM 
# @Author : yefe
# @File : 17005_find_longest_subarray
from typing import List


class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        n = len(array)
        pre = [0] * (n + 1)
        left_hst = dict()
        left_hst[0] = 0
        right_hst = dict()
        for i in range(n):
            if array[i].isdigit():
                pre[i + 1] = pre[i] + 1
            else:
                pre[i + 1] = pre[i] - 1
            if pre[i + 1] not in left_hst:
                left_hst[pre[i + 1]] = i+1
            else:
                right_hst[pre[i + 1]] = i+1
        left, right = -1, -1
        for k, v in left_hst.items():
            if k in right_hst and right_hst[k] - left_hst[k] > right - left:
                left, right = left_hst[k], right_hst[k]

        return array[left: right]


if __name__ == '__main__':
    sol = Solution()
    # array = ["A", "1", "B", "C", "D", "2", "3", "4", "E", "5", "F", "G", "6", "7", "H", "I", "J", "K", "L", "M"]
    # array = ["A", "1"]
    array = ["42","10","O","t","y","p","g","B","96","H","5","v","P","52","25","96","b","L","Y","z","d","52","3","v","71","J","A","0","v","51","E","k","H","96","21","W","59","I","V","s","59","w","X","33","29","H","32","51","f","i","58","56","66","90","F","10","93","53","85","28","78","d","67","81","T","K","S","l","L","Z","j","5","R","b","44","R","h","B","30","63","z","75","60","m","61","a","5","S","Z","D","2","A","W","k","84","44","96","96","y","M"]
    res = sol.findLongestSubarray(array)
    print(res)
