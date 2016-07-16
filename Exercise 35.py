from sys import exit


def gold_room():
    print "This room is full of gold."
    choice = raw_input('>')
    if isanumber(choice):
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you are't greedy"
        exit(0)
    else:
        dead("You greedy bastard")


def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    bear_moved = False
    while True:
        choice = raw_input('>')
        if choice == "take honey":
            dead("The bear looks at you")
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved from the door, you can go through it now."
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."


def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at and you go insane."
    print "Do you flee for your life or eat your head?"
    choice = raw_input('>')
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print why, "Good job!"
    exit(0)


def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"
    choice = raw_input('>')
    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

def isanumber(c):
    b = []
    for i in range(0, 10):
        b.append(str(i))
    b.append('.')
    for j in c:
        if j not in b:
            return False
    if c.count('.') == 1 and c[0] != '.':
        return True
    elif c.count('.') == 0:
        return True
    else:
        return False

start()



##
exit(0) 无错误退出
exit(1) 有错误退出
退出代码是告诉解释器的
Process finished with exit code 0

###
实现了怎么判断raw_input传入的值是否是个数
