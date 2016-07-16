states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

cities['NY'] = 'New Work'
cities['OR'] = 'Portland'

print '-' * 10
print "NY State has:", cities['NY']
print "OR State has:", cities['OR']
print '-' * 10
print "Michigan's abbreviation is:", states['Michigan']
print "Florida's abbreviation is:", states['Florida']
print '-' * 10
print "Michigan has:", cities[states['Michigan']]
print "Florida has:", cities[states['Florida']]
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print '-' * 10
state = states.get('Texas')
if not state:
    print "Sorry, no Texas."
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is : %s" % city

######################
A = {
    "diyi": "first",
    "dier": "second",
    "disan": "third",
    "disi": "fourth"
}
for di, eng in A.items():
    print "zhongwen %s to english is %s" % (di, eng)
得到：
zhongwen dier to english is second
zhongwen disi to english is fourth
zhongwen disan to english is third
zhongwen diyi to english is first
这里面在for里面写入两个变量分别代表key和value，会自动对key进行排序。



关于字典中get的运用
dict.get(key, default=None)
key在字典中查找，key存在时返回key对应的值，key不存在时返回None
A = {
    "diyi": "first",
    "dier": "second",
    "disan": "third",
    "disi": "fourth"
}
B = A.get("disi")
C = A.get("diwu", "buzai")
print B
print C
得到
fourth
buzai
