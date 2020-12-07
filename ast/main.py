# -*- coding: utf-8 -*-
from ast import literal_eval

b = '多汗'.encode('utf-8')
print(b)  # b'\xe3\x81\x82'

s = repr(b)
print(s)
print(type(s))

a = literal_eval(s)
print(a)
print(type(a))

g = a.decode('utf-8')
print(g)
