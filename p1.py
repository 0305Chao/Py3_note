#!/usr/bin/python3
#_*_ coding: UTF-8 _*_

#题目，有四位数字，1，2，3，4 能组成多少个互不相无重复的三位数字？各时多少？
#程序分析，可在百位，十位，个位，数字都是1，2，3，4 组成所有的排列后再去掉不满足条件的排序
for i in range(1,5):
    for j in range(1,5):
    	for k in range(1,5):
    	    if( i != k ) and (i != j) and (j != k):
                print (i,j,k)
