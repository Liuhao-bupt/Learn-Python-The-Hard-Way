print "You enter a dark room with two doors."
door = raw_input('>')
if door == '1':
    print "There is door 1"
    bear = raw_input('>')
    if bear == '1':
        print "bear = 1"
    elif bear == '2':
        print "bear == 2"
    else:
        print "bear != 1 && bear != 2"
elif door == '2':
    print "This is door 2"
else:
    print "this is door 3"
#一定要注意的是raw_input()得到的是一个str类型的变量如果输入的是数字要用int将其变成整数型
a = raw_input('>') 输入12
b = int(a)
b->int,a->str
