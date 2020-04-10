# coding=utf-8
x = input('输入x的值：')
y = input('输入y的值：')

# 不适用临时变量的交换
x, y = y, x
print('交换变量后的x={0}，y={1}'.format(x, y))

# 使用临时变量的交换
tmp = x
x = y
y = tmp
print('交换变量后的x={0}，y={1}'.format(x, y))
