from sys import argv
from os.path import exists
script, from_file, to_file = argv
print "Copying from %s to %s" %  (from_file, to_file)
indata = open(from_file).read()
print "The input file is %d bytes long" % (len(indata))
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()
out_file = open(to_file, 'w')
out_file.write(indata)
print "Alright, all done."
out_file.close()
#len得到一个字符串的长度。
#exists(to_file)如果to_file存在返回True,否则返回False。
