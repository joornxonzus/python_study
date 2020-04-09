# coding = utf-8

sheshiwendu = float(input("输入摄氏温度: "))
huashiwendu = sheshiwendu * 1.8 + 32
print('摄氏温度是{0}，华氏温度是{1}'.format(sheshiwendu, huashiwendu))

huashiwendu = float(input("输入华氏温度: "))
sheshiwendu = (huashiwendu - 32) / 1.8
print('摄氏温度是%0.1f，华氏温度是%0.1f' % (sheshiwendu, huashiwendu))
