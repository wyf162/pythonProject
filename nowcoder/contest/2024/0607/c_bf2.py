# -*- coding : utf-8 -*-
# @Time: 2024/6/7 21:38
# @Author: yefei.wang
# @File: c_bf2.py

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('../../../input.txt', 'r')
sys.stdout = open('../../../jury.txt', 'w')

n = int(input())
s = input().split()
arr = [int(c) for c in s]
m = int(input())


def max_of_min_of_subarrays(arr):
    n = len(arr)

    # Step 1: Initialize arrays to store the previous and next smaller elements
    prev_smaller = [-1] * n
    next_smaller = [n] * n

    # Step 2: Fill prev_smaller array
    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            prev_smaller[i] = stack[-1]
        stack.append(i)

    # Step 3: Fill next_smaller array
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            next_smaller[i] = stack[-1]
        stack.append(i)

    # Step 4: Create an array to store the maximum of minimums for every window length
    max_of_min = [0] * (n + 1)

    # Step 5: Calculate the maximum of minimums for each window length
    for i in range(n):
        length = next_smaller[i] - prev_smaller[i] - 1
        max_of_min[length] = max(max_of_min[length], arr[i])

    # Step 6: Fill the result array
    for i in range(n - 1, 0, -1):
        max_of_min[i] = max(max_of_min[i], max_of_min[i + 1])

    # The result for the largest window
    return max_of_min


arr = max_of_min_of_subarrays(arr)
# print(arr)
for i in range(0, m):
    s = input().split()
    val, minlen, maxlen = int(s[0]), int(s[1]), int(s[2])
    if arr[minlen] >= val:
        print("Yes")
    else:
        print("No")
