from sys import argv
script, filename = argv
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C."
print "If you do want that, hit RETURN."
raw_input('?')
print "Opening the file..."
target = open(filename, 'w')
print "Truncating the file. Goodbye!"
target.truncate()
print "Now I'm going to ask you for three lines."
line1 = raw_input("line1:")
line2 = raw_input("line2:")
line3 = raw_input("line3:")
print "I'm going to write these to the file."
target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')
print "And finally, we close it."
target.close()
#'w'表示建立文件如果存在就清空成空文件，‘w+’就是‘w’加上读操作的能力
 ‘a’表示追加，‘a+’就是‘a’加上读操作的能力，‘r’表示读取文件，‘r+’就是可读可写
 不要同时读写文件，结果通常不如人意。
 例如：a+方式打开文件，之后读取该文件内容。修改读取的内容后重新写入文件，在写入时程序也遇到了IOError错误
 这时要注意在读取文件之后记得要把文件关闭，当你需要写入文件时，要再将文件以w+方式打开写入



