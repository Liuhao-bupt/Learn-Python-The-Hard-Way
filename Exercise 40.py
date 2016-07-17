class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there."])

bulls_on_parade = Song(["They rally around the family.",
                        "With Pockets full of shells"])
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
这节讲得很好
首先Modules Are Like Dictionaries
Dictionaries:
mystuff = {"apple":"I like apple"}
mystuff['apple']
Modules:
#this goes in mystuff.py
def apple():
  print "I like apple."

import mystuff
mystuff.apple()

Classes Are Like Modules


class mystuff(object):
  def __init__(self):
    self.tangerine = "A thousand years"
  def apple(self):
    print "I like apples"

thing = mystuff()
thing.tangerine
thing.apple()
