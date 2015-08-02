class Living_Things:
  def __init__(self,name):
    self.name=name
  def move(self):
    print "I am moving"
  def breathe(self):
    print "I am breathing"
  def my_name(self):
    print "my name is {}".format(self.name)


class Human(Living_Things):
  def thinking(self):
    print"i am thinking"

class Cat(Living_Things):
  def climbing_a_roof(self):
    print "i am climbing roof"

class Bird(Living_Things):
  def flying(self):
    print "i am flying"


jo=Human("jo")
catro=Cat("catro")
beo=Bird("beo")

jo.move()
catro.move()
beo.move()
print ""
jo.thinking()
catro.climbing_a_roof()
beo.flying()
