#_*_ coding: UTF-8 _*_

num = float(input('请输入一个数字： '))

#num 就是 mun 的 0.5次方，比如 a = 10,b = 20 ,a ** b 就是 10的20次方
num_sqrt = num **0.5 #一个数的一半的一半
print ('%0.2f 的平方根为 %0.2f' %(num, num_sqrt))

#复数平方
import cmath
# cmath(complex math) 模块的sqrt() 方法
num = int(input('请输入一个数字: '))

num_sqrt = cmath.sqrt(num)
print ('{0} 的平方为 {1:0.3f} + {2:0.3f}j'.format(num, num_sqrt.real, num_sqrt.imag))
