# _*_ coding: utf-8 _*_
# @Time : 2022/2/25 下午9:27 
# @Author : wangyefei
# @File : 537_complex_number_multiply.py


class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        real1, imag1 = self.translate(num1)
        real2, imag2 = self.translate(num2)

        real3 = real1 * real2 - imag1 * imag2
        imag3 = real1 * imag2 + real2 * imag1
        return str(real3) + '+' + str(imag3) + 'i'

    def translate(self, num):
        i = 0
        if num[i].isdigit():
            real_sign = 1
        else:
            real_sign = -1
            i += 1
        real = 0
        while num[i].isdigit():
            real = real * 10 + int(num[i])
            i += 1
        i += 1
        if num[i].isdigit():
            imag_sign = 1
        else:
            imag_sign = -1
            i = i+1
        imag = 0
        while num[i].isdigit():
            imag = imag * 10 + int(num[i])
            i += 1
        return real * real_sign, imag * imag_sign


if __name__ == '__main__':
    sol = Solution()
    num1 = "1+-1i"
    num2 = "1+-1i"
    ret = sol.complexNumberMultiply(num1, num2)
    print(ret)
