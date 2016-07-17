import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []
PHRASES = {
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
        "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":
        "Set *** to an instance of class %%%.",
    "***.***(@@@)":
        "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."
}
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASES_FIRST = True
else:
    PHRASES_FIRST = False

for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())


def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                   random.sample(WORDS,snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []
    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1, 3)
        param_names.append('.'.join(random.sample(WORDS,param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]
        for word in class_names:
            result = result.replace("%%%", word, 1)
        for word in other_names:
            result = result.replace("***", word, 1)
        for word in param_names:
            result = result.replace("@@@", word, 1)
        results.append(result)
    return results

try:
    while True:
        snippets = PHRASES.keys()
        random.shuffle(snippets)
        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASES_FIRST:
                question, answer = answer, question
            print question
            raw_input('>')
            print "ANSWER: %s\n\n" % answer
except EOFError:
    print "\nBye"

关于sys.argv
sys.argv[]获取命令行参数，sys.argv[0]表示文件本身路径，参数从argv[1]

关于read,readline,readlines
read = open("test.txt").read()
readl = open("test.txt").readline()
readls = open("test.txt").readlines()
print type(read), read
print type(readl), readl
print type(readls), readls

<type 'str'> liuhao
fighting
best
<type 'str'> liuhao

<type 'list'> ['liuhao\n', 'fighting\n', 'best'] 是个list

关于strip
A = "\t      liuhaofightingjiushi\t      "
print A
B = A.strip()
print A
print B
A = "1345"
B = A.strip('12')
print A
print B
得到
	      liuhaofightingjiushi	      
	      liuhaofightingjiushi	      
liuhaofightingjiushi
1345
345
要说的是strip()默认括号内包括'\n' '\t' '\r' ' ',只要在其中位于开头或结尾的就删除
同理strip（‘12’）,就是只要开头或结尾是'1' '2'中的就删除


关于random
print random.random()生成一个[0,1)之间的随机数
print random.uniform(a, b)生成一个[a,b]或[b,a]之间的的随机数
print random.randint(0, 10)生成一个[a,b]之间的随机数，大小位置不能变。
print random.randrange(0, 100, 2)在[0,100)之间以2为间隔随机取一个数，相当于取0-100之间的偶数
A = ['a', 'b', 'c', 'e']
print random.choice(A) 从序列中随机选一个元素
A = ['a', 'b', 'c', 'e']
random.shuffle(A)随机打乱一个序列
print A ----> ['b', 'e', 'c', 'a']
A = ['a', 'b', 'c', 'e', 'f', 'd', 'g', 'h']
s = random.sample(A, 4)从序列A中随机选出4个元素
print s------->['a', 'f', 'e', 'c']

关于captialize   返回字符串的一个副本，只有第一个字母大写。
A = "ggggggggggggg"
print A.capitalize()  
print A
------>
Ggggggggggggg
ggggggggggggg
关于count
A = "abcdegggabc"
print A.count("abc")--------->2
同样也可以指定，查找位置
A = "aaaa"
print A.count("a", 0, 3)---->3,可知不包括最后的位置。

关于replace
A = "aaaa"
print A.replace('a', 'b')
print A  
得到：
bbbb
aaaa
同样可知道替换的次数
A = "aaaa"
print A.replace，这里的3次代表的是不多于3次
print A
得到：
bbba
aaaa


A = [1, 2, 3, 4]
B = [5, 6, 7, 8]
C = []
for i in A, B:##相当于一个列表[A, B]
    C.append(i)#执行两次，i一次是A，一次是B
print C
[[1, 2, 3, 4], [5, 6, 7, 8]]

A = [1, 2, 3, 4]
B = [5, 6, 7, 8]
A, B = B, A
print A
print B
a = 3
b = 4
a, b = b, a
print a
print b
得到

[5, 6, 7, 8]
[1, 2, 3, 4]
4
3
交换了两个变量的值
