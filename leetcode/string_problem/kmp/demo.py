# _*_ coding: utf-8 _*_
# @Time : 2022/11/03 10:10 PM 
# @Author : yefe
# @File : demo


# Python Version
def prefix_function(s):
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi


def kmp(s, t):
    pi = prefix_function(s + "#" + t)
    for i in range(len(pi)):
        if pi[i] == len(s):
            return True

    return False


if __name__ == '__main__':
    s = "abce"
    t = "abcd"
    print(kmp(s, t))
