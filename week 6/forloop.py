#print 1 2 3 4 5
print("# print 1 2 3 4 5")
for loop in range (1,6):
  print loop,
print "\n"

#print 0 2 4 6 8
print("# print 0 2 4 6 8")
for loop in range (0,10,2):
  print loop,
print "\n"

#print 5 4 3 2 1
print("# print 5 4 3 2 1 ")
for loop in range (5,0,-1):
  print loop,
print "\n"

# print 20 15 10 5 0
print("# print 20 15 10 5 0")
for loop in range (20,-1,-5):
  print loop,
print "\n"

#print word that user input 5 times use "for"
word=raw_input("word:")
loop=5
for loop in range (1,6):
  print '{} {}'.format(word,loop)
print "\n"

word=raw_input("word:")
loop=5
for loop in range (5,0,-1):
  print '{} {}'.format(word,loop)
print "\n"


word=raw_input("word:")
loop=5
for loop in range (20,-1,-5):
  print '{} {}'.format(word,loop)
print "\n"


word=raw_input("word:")
loop=5
for loop in range (0,21,5):
  print '{} {}'.format(word,loop)
print "\n"

#print word as many  as user want use "for"
word=raw_input("word:")
many=input("how many times:")
loop=1
for loop in range (many,0,-1):
  print word
print "\n"



word=raw_input("word:")
many=input("how many times:")
loop=1
for loop in range (many,0,-1):
   print '{} {}'.format(word,loop)
print "\n"

word=raw_input("word:")
many=input("how many times:")
loop=1
for loop in range (1,many+1,1):
   print '{} {}'.format(word,loop)
print "\n"

