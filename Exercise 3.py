# -*- coding: utf-8 -*-
print "I will now count my chickens:"

print "Hens", 25 + 30 / 6
print "Roosters", 100 - 25 * 3 % 4

print "Now I will count the eggs:"

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

print "Is it true that 3 + 2 < 5 - 7?"

print 3 + 2 < 5 - 7

print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it  less or equal?", 5 <= -2
print 5 / 2
print 5.0 / 2
print -5 / 2
#关于python中的除法
1.普通除法
  浮点数相除会得到精确值，整数相除会得到小于等于其值的最大整数如5/2=2,-5/2=-3
2.地板除法
  操作符“//”,执行地板除，在整数上与“/”无区别，在浮点数除上会得到一个舍去了小数部分的数字 5.0//2=2.0,-5.0//2=-3.0
3.精确除法
  除法总是会返回真实的商，不管是整型还是浮点型
  执行from __future__ import division
  1/2=0.5,1.0/2=0.5
4.内建函数
  divmod(a,b)
  返回(a//b,a%b)
  
