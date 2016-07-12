# -*- coding: utf-8 -*-
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
'''
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print "I\"m very young"
for i in ["/", "_", "|", "\\\\", "|"]:
    print "%s\r" % i
# \ 是转意字符
例如print "\\" -> \
    print ' I\'m very good ' -> I'm very good
    print "\\\" 这样是错误的。因为第二个\被第一所转意，那么”被第三个\所转意，这样就少了一个”。
三个单引号和三个双引号的效果是一样的。
