#_*_ coding: UTF-8 _*_

x = input('请输入 x 值：')
y = input('请输入 y 值：')

#创建临时变量并交换
temp = x
x = y
y = temp

print ('交换后的x的值为：{}'.format(x))
print ('交换后的y的值为: {}'.format(y))

#创建固定变量

x = input('请输入 x 值: ')
y = input('请输入 y 值：')

#不适用临时变量
x,y = y,x

print ('交换后的x的值为: {}'.format(x))
print ('交换后的y的值为：{}'.format(y))
