# _*_ coding: utf-8 _*_
# @Time : 2022/12/11 3:07 PM 
# @Author : yefe
# @File : 6259_Allocator

class Allocator:
    def __init__(self, n: int):
        self.a = [0] * n

    def allocate(self, size: int, mID: int) -> int:
        cnt = 0
        for i, id in enumerate(self.a):
            if id:
                cnt = 0
            else:
                cnt += 1
                if cnt == size:
                    self.a[i - size + 1: i + 1] = [mID] * size
                    return i - size + 1
        return -1

    def free(self, mID: int) -> int:
        cnt = 0
        for i, id in enumerate(self.a):
            if id == mID:
                cnt += 1
                self.a[i] = 0
        return cnt


if __name__ == '__main__':
    cmds = ["Allocator", "allocate", "allocate", "allocate", "free", "allocate", "allocate", "allocate", "free", "allocate", "free"]
    parms = [[10], [1, 1], [1, 2], [1, 3], [2], [3, 4], [1, 1], [1, 1], [1], [10, 2], [7]]

    allocator = Allocator(parms[0][0])
    for cmd, parm in zip(cmds[1:], parms[1:]):
        ret = getattr(allocator, cmd)(*parm)
        print(ret)
