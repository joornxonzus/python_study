# coding = utf - 8

num = float(input('输入一个数字：'))
if num > 0:
    print('正数')
elif num == 0:
    print('零')
else:
    print('负数')

if num >= 0:
    if num > 0:
        print('positive')
    else:
        print('zero')
else:
    print('negative')
