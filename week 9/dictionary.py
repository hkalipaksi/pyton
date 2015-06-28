#initaalize empty dictionary
menu_dictionary={}

#add item to dictionary dictionary_name[key]=value
menu_dictionary['nasi']=1000
print menu_dictionary

#initialize dictionary with value dictionary_name={key value,key value}
my_dictionary={'merah':'red','blue':'biru'}
print my_dictionary


print "Add new item to dictionary"
key=raw_input("input a key:")
my_dictionary[key]=raw_input("input a value:")
print my_dictionary
