# _*_ coding: utf-8 _*_
# @Time : 2022/05/29 2:56 PM 
# @Author : yefe
# @File : demo


def construct_tree(inputs, seg_tree, low, high, pos):
    if low == high:
        seg_tree[pos] = inputs[low]
        return
    mid = (low + high) // 2
    construct_tree(inputs, seg_tree, low, mid, 2 * pos + 1)
    construct_tree(inputs, seg_tree, mid + 1, high, 2 * pos + 2)
    seg_tree[pos] = min(seg_tree[2 * pos + 1], seg_tree[2 * pos + 2])


def range_min_query(seg_tree, qlow, qhigh, low, high, pos):
    if qlow<=low and qhigh>=high:
        return seg_tree[pos]
    if qlow>high or qhigh<low:
        return 99
    mid = (low+high)//2
    return min(range_min_query(seg_tree, qlow, qhigh, low, mid, 2*pos+1),
               range_min_query(seg_tree, qlow, qhigh, mid+1, high, 2*pos+2))


if __name__ == '__main__':
    inputs = [-1, 2, 4, 0]
    n = len(inputs)
    seg_tree = [0] * (len(inputs) * 4)
    construct_tree(inputs, seg_tree, 0, 3, 0)
    print(seg_tree)

    for qlow in range(n):
        for qhigh in range(qlow, n):
            ret = range_min_query(seg_tree, qlow, qhigh, 0, 3, 0)
            print(qlow, qhigh, ret)
