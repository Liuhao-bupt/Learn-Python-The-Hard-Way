ten_things = "Apples Oranges Crows Telephone Light Sugar"
print "Wait there are not 10 ten things in that list. Let's fix that."
stuff = ten_things.split(' ')
more_stuff = ["Days", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding:", next_one
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)

print "There we go:", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])
关于join函数的运用
join将字符串，列表，元祖中的元素以指定字符连接起来
A = ['a', 'b', 'c']
B = ' '.join(A)
print A
print B
得到
['a', 'b', 'c']
a b c
