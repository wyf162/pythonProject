# _*_ coding: utf-8 _*_
# @Time : 2022/4/5 下午3:06 
# @Author : wangyefei
# @File : 17018_shortest_seq.py
from typing import List


class Solution:
    def shortestSeq(self, big: List[int], small: List[int]) -> List[int]:
        target_dict = {k: 0 for k in small}
        diff = 0
        i, j = 0, 0
        ret = []
        while i <= j < len(big):
            while diff < len(small) and j < len(big):
                if big[j] in target_dict:
                    if target_dict[big[j]] == 0:
                        diff += 1
                    target_dict[big[j]] += 1
                j += 1

            while i <= j and diff == len(small):
                if not ret:
                    ret = [i, j - 1]
                elif ret[1] - ret[0] > j - i - 1:
                    ret = [i, j - 1]

                if big[i] in target_dict:
                    target_dict[big[i]] -= 1
                    if target_dict[big[i]] == 0:
                        diff -= 1
                i += 1

        return ret


if __name__ == '__main__':
    sol = Solution()
    # big = [7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7]
    # small = [1, 5, 9]
    # big = [521704, 897261, 279103, 381783, 668374, 934085, 254258, 726184, 496153, 804155]
    # small = [897261, 934085, 381783, 496153]
    # big = [842, 336, 777, 112, 789, 801, 922, 874, 634, 121, 390, 614, 179, 565, 740, 672, 624, 130, 555, 714, 9, 950,
    #        887,
    #        375, 312, 862, 304, 121, 360, 579, 937, 148, 614, 885, 836, 842, 505, 187, 210, 536, 763, 880, 652, 64, 272,
    #        675,
    #        33, 341, 101, 673, 995, 485, 16, 434, 540, 284, 567, 821, 994, 174, 634, 597, 919, 547, 340, 2, 512, 433,
    #        323, 895,
    #        965, 225, 702, 387, 632, 898, 297, 351, 936, 431, 468, 694, 287, 671, 190, 496, 80, 110, 491, 365, 504, 681,
    #        672,
    #        825, 277, 138, 778, 851, 732, 176]
    # small = [950, 885, 702, 101, 312, 652, 555, 936, 842, 33, 634, 851, 174, 210, 287, 672, 994, 614, 732, 919, 504,
    #          778, 340,
    #          694, 880, 110, 777, 836, 365, 375, 536, 547, 887, 272, 995, 121, 225, 112, 740, 567, 898, 390, 579, 505,
    #          351, 937,
    #          825, 323, 874, 138, 512, 671, 297, 179, 277, 304]
    big = [1, 2, 1, 2, 1, 2]
    small = [1, 2]
    ret = sol.shortestSeq(big, small)
    print(ret)
