# mtx = [
#     [3, 1, 0],
#     [6, 4, 2],
#     [8, 7, 5]
# ]
#
# # c = i - j
#
# n, m = 3, 3
# for c in range(-m + 1, n):
#     for j in range(0, m):
#         i = j + c
#         if 0 <= i < n:
#             print(mtx[i][j], end=' ')


mtx = [
    [5, 2, 0],
    [7, 4, 1],
    [8, 6, 3]
]

# c = i - j
n, m = 3, 3
for c in range(-m + 1, n):
    for j in range(m-1, -1, -1):
        i = j + c
        if 0 <= i < n:
            print(mtx[i][j], end=' ')

