# -*- coding: utf-8 -*-
print "How old are you?",
age = raw_input()
print "How tall are you ?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()
print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)
raw_input_A = raw_input("raw_input:")
input_A = input("Input:")
raw_input_B = raw_input("raw_input:")
print type(raw_input_B)
input_B = input("input:")
print type(input_B)
int_B = int(raw_input_B)
print type(int_B)
#
关于输入 raw_input() 和 input()
input_A = input("Input:") 输入 abc 报错， 必须输入 “abc” ；输入123，格式int
raw_input_B = raw_input("raw_input:") 输入abc正确；输入123，格式str
raw_input()将所有的输入当做字符串看待
input()他希望读取一个合法的python表达式
对于两者在书里面有这样的话：“The input() function will try to convert things you enter as if they were Python code, 
but it has security problems so you should avoid it.”
也就是建议用raw_input()
如果输入的数字变成了str可以再将这个转换成int
python string 和 int 转换
a = 10
str1 = str(a)
a = '10'
int1 = int(a) 
