def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words


def sort_words(words):
    return sorted(words)


def print_first_word(words):
    word = words.pop(0)
    print word


def print_last_word(words):
    word = words.pop(-1)
    print word


def sort_sentences(sentence):
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    words = sort_sentences(sentence)
    print_first_word(words)
    print_last_word(words)
#
第一个 pop
       A = [1,2,3,4,5]
       A.pop()   ->  5
       A.pop(0)  ->  1
       A.pop(-1) ->  5
       
第二个 sort
       A = [2,1,3,8,5,6]
       A.sort()不返回任何东西，只是改变了A的排序 A -> [1,2,3,5,6,8]
       y=sorted(x)
       y=[1,2,3,5,6,8]  A不变。
