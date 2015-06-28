print("program")
list_menu=['nasi','ayam']
def program ():
  print "1.show menu"
  print "2.input menu"
  print "3.Delete menu"
  print "4.Rename menu"
  print "5.Exit"
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

  elif choice ==3:
    delete()
    any_key()
    program()

  elif choice ==4:
    rename()
    any_key()
    program()

  elif choice ==5:
    exit()

def out():
  print "\n\n Our Food Menu"
  idx=0
  for menu in list_menu:
    idx=idx+1
    print "{} {}".format(idx,menu)

def inp():
  add=raw_input("add a food name:")
  list_menu.append(add)

def delete():
  remove=raw_input("Delete a food name:")
  list_menu.remove(remove)

def rename():
  rename=raw_input("input a food name to be renamed:")
  update=list_menu.index(rename)
  list_menu[update]=raw_input("add a new food name for {}:".format(rename))
  
def any_key():
  ket=raw_input("\npress any key...")

program()

