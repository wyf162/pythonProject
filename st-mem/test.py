# _*_ coding: utf-8 _*_
# @Time : 2022/1/15 下午9:37 
# @Author : wangyefei
# @File : test.py

print(__name__)
print(memoryview(b'foo'))
print(type(memoryview))
print(isinstance(b'foo', memoryview))
mv = memoryview(b'foo')
print(mv[1:2].tobytes())
print(bytes(mv))
print(isinstance(mv, memoryview))