# _*_ coding: utf-8 _*_
# @Time : 2022/05/18 9:37 PM 
# @Author : yefe
# @File : 273_number_to_words

singles = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
thousands = ["", "Thousand", "Million", "Billion"]


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "zero"

        def recursion(num: int) -> str:
            s = ""
            if num == 0:
                return s
            elif num < 10:
                s += singles[num] + " "
            elif num < 20:
                s += teens[num - 10] + " "
            elif num < 100:
                s += tens[num // 10] + " " + recursion(num % 10)
            else:
                s += singles[num // 100] + " Hundred " + recursion(num % 100)
            return s

        s = ""
        unit = int(1e9)
        for i in range(3, -1, -1):
            cur_num = num // unit
            if cur_num:
                num -= cur_num * unit
                s += recursion(cur_num) + thousands[i] + " "
            unit //= 1000
        print(s)
        return s.strip()


if __name__ == '__main__':
    sol = Solution()
    num = 12345
    ret = sol.numberToWords(num)
    print(ret)
