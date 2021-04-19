# coding = utf - 8
import re

m = re.match('foo', 'food is foo')
print(type(m))
if m is not None:
    print(m.group())

m = re.findall('foo', 'food is foo')
print(type(m))
if m is not None:
    print(m.__len__())
    print(m)




