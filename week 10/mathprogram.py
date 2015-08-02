def program ():
  print "\n"
  print "Math program"
  print "1.Addition"
  print "2.Substraction"
  print "3.Multification"
  print "4.division"
  print "5.Exit"
  choice=input("What's your choice:")
  if choice==1:
    print "Addition"
    a=first()
    b=second()
    add  (a,b)
    program()
  elif choice==2:
    a=first()
    b=second()
    substract   (a,b)
    program()
  elif choice==3:
    a=first()
    b=second()
    multiply(a,b)
    program()
  elif choice==4:
    a=first()
    b=second()
    divide(a,b)
    program
  elif choice==5:
    exit()

def first ():
  inp=input("enter a first number:")
  return inp

def second ():
  inp=input("enter a second number:")
  return inp


def add (a,  b):
  print " ADDING {} + {} = {}".format (a,b,a + b)  

def substract (a, b):
  print " SUBSTRACTING {} - {} = {}".format(a,b,a - b)

def multiply (a, b):
  print " MULTIPLYING {} x {} = {}".format(a,b,a * b)

def divide (a, b):
  print " DIVIDEING {} : {} = {}".format(a,b,a / b)

program()
