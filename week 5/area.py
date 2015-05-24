close="no"
while close != "yes":  
  print("Welcome to my program")
  print("menu:")
  print("1.calculate area of triangle")
  print("2.calculate area of square")
  print("3.calculate area of rectangle")
  choice=input("your choice:")
  if choice==1:
    print("choice is 1")
    print("program to calculate area of triangle")
    base=input("input base:")
    height=input("input height:")
    areatriangle=(base*height)/2
    print("area of triangle:{0}".format(areatriangle))
    print("finish")
  elif choice==2:
    print("program to calculate area of square")
    print("choice is 2")
    side=input("input side:")
    areasquare=side*side
    print("area of square:{0}".format(areasquare))
    print("finish")
  elif choice==3:
    print("program to calculate area of rectangle")
    print("choice is 3")
    width=input("input widht:")
    height=input("input height:")
    arearectangle=width*height
    print("area of rectangle:{0}".format(arearectangle))
  close=raw_input("close? (yes/no):")  
