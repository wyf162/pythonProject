# -*- coding : utf-8 -*-
# @Time: 2024/1/5 0:05
# @Author: yefei.wang
# @File: 1714D2.py

for _ in range(int(input())):
    T = input()
    N = int(input())
    subs = [input() for _ in range(N)]

    end = 0
    steps = []
    while end < len(T):
        best_end = end
        best_w = -1
        best_index = -1
        for start in range(end + 1):
            for i, sub in enumerate(subs):
                if T[start:start + len(sub)] == sub:
                    new_end = start + len(sub)
                    if new_end > best_end:
                        best_end = new_end
                        best_w = i + 1
                        best_index = start + 1
        if best_end == end:
            print(-1)
            break
        steps.append((best_w, best_index))
        end = best_end
    if end >= len(T):
        print(len(steps))
        for a, b in steps:
            print(a, b)
