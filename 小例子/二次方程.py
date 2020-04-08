import cmath

a = float(input('input a:'))
b = float(input('input b:'))
c = float(input('input c:'))

d = (b ** 2) - 4 * a * c

sol1 = (-b - cmath.sqrt(d)) / (2 * a)
sol2 = (-b + cmath.sqrt(d)) / (2 * a)

print('结果是：{0},{1}'.format(sol1, sol2))
