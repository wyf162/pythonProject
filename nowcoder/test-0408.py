# _*_ coding: utf-8 _*_
# @Time : 2022/4/8 下午10:20 
# @Author : wangyefei
# @File : test-0408.py
def main2(l,r,a):
    ret = 0
    i = 1
    while i*a<=r-l:
        ret += (r-l-i*a+1)
        i += 1
    return ret


def main3(l,r,a):
    h = (r-l)//a
    up = (r-l-h*a+1)
    down = (r-l-a+1)
    return (up+down)*h//2


def main(nums, edges, k):
    n = len(nums)
    degrees = [0]*(n+1)
    for edge in edges:
        s, t = edge
        degrees[s] += 1
        degrees[t] += 1
    densities = []
    for i in range(n):
        densities.append((i+1, nums[i]))

    l, r = -1, max(nums)+1

    while l<=r:
        m = (l+r)>>1
        if check(edges, nums, m)<=k:
            r = r-1
        else:
            l = l+1
    return l


def check(edges, nums, m):
    ret = 1
    for edge in edges:
        s, t = edge
        if nums[s-1]>=m or nums[t-1]>=m:
            ret += 1
    return ret


if __name__ == '__main__':
    nums = [1,2,3,4,5]
    edges = [[1,2],[2,5],[5,3],[4,1]]
    k = 6
    ret = main(nums, edges, k)
    print(ret)

    # l,r,a=1,5,1
    # ret = main(l,r,a)
    # print(ret)