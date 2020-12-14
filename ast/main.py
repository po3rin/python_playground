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

z = r'\xe7\xb2\xbe\xe7\xa5\x9e\xe7\x9a\x8'
b = literal_eval(f"b'{z}'")
v = b.decode('sjis')
print(v)
