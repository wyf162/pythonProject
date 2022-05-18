# _*_ coding: utf-8 _*_
# @Time : 2022/05/17 12:23 AM 
# @Author : yefe
# @File : 1172_DinnerPlates
import heapq


class DinnerPlates:

    def __init__(self, capacity: int):
        self.stks = []
        self.capacity = capacity
        self.hq = []
        heapq.heapify(self.hq)
        self.hq2 = []
        heapq.heapify(self.hq2)

    def push(self, val: int) -> None:
        if not self.stks:
            self.stks.append(list())
            idx = 0
            self.stks[idx].append(val)
            if len(self.stks[idx])<self.capacity:
                    heapq.heappush(self.hq, idx)
            heapq.heappush(self.hq2, -1*idx)
        else:
            if self.hq:
                idx = heapq.heappop(self.hq)
                self.stks[idx].append(val)
                if len(self.stks[idx])<self.capacity:
                    heapq.heappush(self.hq, idx)
                heapq.heappush(self.hq2, -1 * idx)
            else:
                self.stks.append(list())
                idx = len(self.stks)-1
                self.stks[idx].append(val)
                if len(self.stks[idx])<self.capacity:
                    heapq.heappush(self.hq, idx)
                heapq.heappush(self.hq2, -1 * idx)

    def pop(self) -> int:
        if self.stks:
            while self.hq2:
                idx = -1 * heapq.heappop(self.hq2)
                if len(self.stks[idx])>1:
                    heapq.heappush(self.hq2, -1*idx)
                    if len(self.stks[idx]) == self.capacity:
                        heapq.heappush(self.hq, idx)
                    return self.stks[idx].pop()
                elif len(self.stks[idx])==1:
                    if len(self.stks[idx]) == self.capacity:
                        heapq.heappush(self.hq, idx)
                    return self.stks[idx].pop()
            return -1
        else:
            return -1

    def popAtStack(self, index: int) -> int:
        if index<len(self.stks) and self.stks[index]:
            if len(self.stks[index])==self.capacity:
                heapq.heappush(self.hq, index)
            return self.stks[index].pop()
        else:
            return -1


if __name__ == '__main__':
    dinner_plates = DinnerPlates(1)
    dinner_plates.push(1)
    dinner_plates.push(2)
    ret = dinner_plates.popAtStack(1)
    print(ret)
    ret = dinner_plates.pop()
    print(ret)
    dinner_plates.push(1)
    dinner_plates.push(2)
    ret = dinner_plates.pop()
    print(ret)
    ret = dinner_plates.pop()
    print(ret)
