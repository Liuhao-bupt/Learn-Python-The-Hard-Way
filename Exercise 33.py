i = 0
numbers = []
while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)
    i += 1
    print "Numbers now:", numbers
    print "At the bottom i is %d" % i

print "The numbers:"
for num in numbers:
    print num


关于range
range(1,5)->[1,2,3,4]不包括5.
range(1,5,2)-->[1,3]  1到5间隔为2不包括5.
range(5)-->[0,1,2,3,4] 不包括5，从0开始算起. 
