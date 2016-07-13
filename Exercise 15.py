from sys import argv
script, filename = argv
txt = open(filename)
print "Here's your file %r:" % filename
print txt.read()
print "Type the filename again:"
file_again = raw_input(">")
txt_again = open(file_again)
print txt_again.read()

#
1.用python open函数打开文件
  x = open(r"D:/pycharm/PyCharm 2016.1.4/build.txt")
2.open()函数打开文件模式参数常用值有哪些
  r表示读模式
  w表示写模式
  b表示二进制模式
  a表示追加模式
3.python文件写入操作
  f = open("a.txt", 'w')
  f.write("hello,")
  f.write("nihao.")
  f = open("a.txt")
  print f.read()
  f.close()
4.python文件读取操作方法
  f = open("a.txt",'r')程序默认是r，所以读的时候也可以不写r
  f.read(5) ()内填入要读取的字符数。
  read()表示读取全部内容
  readline()表示逐行读取。
  
  
