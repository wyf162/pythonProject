import sys
import random

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def psort(array):
    if len(array) <= 1:
        return array

    pivot_index = random.randint(0, len(array) - 1)
    pivot = array[pivot_index]
    left = []
    right = []

    for i, ele in enumerate(array):
        if i == pivot_index:
            continue

        A, C, x = ele
        if A * pivot[1] > pivot[0] * C:
            left.append(ele)
        elif A * pivot[1] < pivot[0] * C:
            right.append(ele)
        else:
            if x > pivot[2]:
                right.append(ele)
            elif x < pivot[2]:
                left.append(ele)

    return psort(left) + [pivot] + psort(right)


n = int(input())
lst = []

for i in range(n):
    a, b = map(int, input().split())
    lst.append([a, a + b, i + 1])

lst = psort(lst)

for i in range(n):
    print(lst[i][2], end=" ")
