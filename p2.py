#!/usr/bin/python3
#_*_ coding: UTF-8 _*_

#题目：企业发放奖金根据利润提成，利润(i) 低于10万元时，奖金可提成10%；利润高于10万低于20万，低于10万元的部分
#安10%提成，高于10万的部分，安0.7%；20万到40万之间时，高于20万元的部分，可按照5%；40万元到60万元的部分，可提成
#3%；60万元到100万元之间时，高于60万元的部分，可提成1.5%，高于100万元，超过100万元的部分安1%提成，从键盘
#输入当月的利润，求应发奖金总数。

#程序分析，请利用数轴来分界，定位，注意定义时需要把奖金定义成长整型。

i = (int(input('净利润：')))
#从大到小
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0

for idx in range(0,6):
    if i>arr[idx]:
    	r+=((i-arr[idx]) * rat[idx])
    	print ((i-arr[idx]) * rat[idx])
    	i = arr[idx]
print('总利润为: ' , r)
