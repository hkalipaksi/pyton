print("program")
list_menu=['nasi','ayam']
def program ():
  print "1.show menu"
  print "2.input menu \n"
  print ""
  choice=input("whats your choice:")
  if choice==1:
    out()
    any_key()
    program()

  elif choice ==2:
    inp()
    any_key()
    program()

def out():
  print "\n\n Our Food Menu"
  idx=0
  for menu in list_menu:
    idx=idx+1
    print "{} {}".format(idx,menu)

def inp():
  add=raw_input("add a food name:")
  list_menu.append(add)

def any_key():
  ket=raw_input("\npress any key...")

program()

