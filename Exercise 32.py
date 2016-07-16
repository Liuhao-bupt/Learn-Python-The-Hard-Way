hairs = ['brown', 'blond', 'red']
eyes = ['brown', 'blue', 'green']
weights = [1, 2, 3, 4]
the_count = [1, 2, 3, 4, 5]
fruits = ['apple', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
for number in the_count:
    print "This is count %d" % number
for fruit in fruits:
    print "A fruit of type: %s" % fruit
for i in change:
    print "I got %r" % i
elements = []
for i in range(0, 6):
    print "Adding %d to the list." % i
    elements.append(i)
for i in elements:
    print "Element was %d" % i
    
    
###
test = [1, 't', 3, 's']
for i in test:
    tp = type(i)
    print"%r is %r" % (i, tp)
得到
1 is <type 'int'>
't' is <type 'str'>
3 is <type 'int'>
's' is <type 'str'>

关于list的操作：
通过索引访问从下表0开始

利用+
test = [1, 't', 3, 's']
a = [4, 5]
test += a
print test--->[1, 't', 3, 's', 4, 5]
利用*
a = [4, 5]
a *= 2
print a------>[4, 5, 4, 5]

len取长度
a = [4, 5]
a *= 2
print len(a)----->4

max 和 min
test = [1, 2, 8, 6, 4, 9]
print max(test)  -> 9
print min(test)  -> 1
关于python中字符串的比较“字符串也好，列表也好，都是可迭代的对象，先比较第一个元素，大小关系即为对象关系大小，
如果相等就继续向下，先终止迭代的认为是小的。

append
A = [1, 2, 3]
A.append(4)
print A   [1,2,3,4]


count

A = [1, 2, 3, 3, 4, 4, 4, 4, 3]
b = A.count(4)
print b   ---> 4

index找出元素在列表中第一次出现的下标数
A = [1, 2, 3, 3, 5, 4, 4, 4, 3]
b = A.index(4)
print b  --->  5

insert 在指定位置插入元素，并将包括这个元素及其后的元素往后移
A = [1, 2, 3]
A.insert(0, 9)
print A  ->[9, 1, 2, 3]
A.insert(3,9) -> [1, 2, 3, 9]
A.insert(-1,9)  ->[1, 2, 9, 3]

reverse 反转
A = [1, 2, 3]
A.reverse()
print A--->[3,2,1]

如果
A = [1, 2, 3]
B = A.reverse()
print B  ---->none   reverse函数不返回值


extend 用新列表扩展原来的列表
A = [1, 2, 3]
B = [4, 5, 6]
A.extend(B)
print A -->[1,2,3,4,5,6]


remove一出第一个匹配的元素
A = [1, 2, 3, 1]
A.remove(1)
print A---->[2,3,1]
