class Living_Things:
  def __init__(self,name):
    self.name=name
  def move(self):
    print "I am moving"
  def breathe(self):
    print "I am breathing"
  def my_name(self):
    print "my name is {}".format(self.name)


cathy=Living_Things("cathy")
cathy.my_name()

jon=Living_Things("jon")
jon.my_name

