# -*- coding: utf-8 -*-
from sys import argv
'''script, first, second, third = argv
print "The script is called:", script
print "Your first variable is:", first
print "You second variable is:", second
print "You third variable is:", third
age = raw_input("age:")
print age'''
script = "python"
user_name = "liuhao"
prompt = '>'
print "My name is %s, and you know I am the %s script." % (user_name, script)
print "do u like me ?"
like = raw_input(prompt)
print "how old are you ?"
age = raw_input(prompt)
print """
OK,you said you %r me very much. you are %r years old.""" % (like, age)
#sys.argv和raw_input()的区别
argv是在运行脚本文件的时候连同文件名一起输入，比如：python ex.py first 2nd 3rd
raw_input则是在程序运行中应程序要求输入的
