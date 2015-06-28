#create list if "menu"
list_menu=['nasi','ayam','kentang']
print ""

#['nasi','ayam','kentang']
print list_menu
print ""

#"append"adding an item to a list
#use name_of_list.append(item)
food=raw_input("input a food to be added to list:")
list_menu.append(food)
print list_menu

#"insert"adding an item to a list on given index
#use name_of_list.insert(index,item)
food=raw_input("input a food to be added to list:")
index=input("index:")
list_menu.insert(index,food)
print list_menu
print ""

#"index"get  item index on a list
#use name_of_list.index(item)
food=raw_input("input a food to be added to list:")
idx=list_menu.index(food)
print "{}\'s index is {}".format(food,idx)
print ""

#"remove"remove an item on a list
#use name_of_list.remove(item)
print "menu before remove: {}".format(list_menu)
food=raw_input("input a food to be removed:")
list_menu.remove(food)
print "menu after remove: {}".format(list_menu)
