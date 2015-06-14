many=input("how many times:")
loop=100
for loop in range (1,many+1,1):
  if loop%3==0 and loop%5==0:
    print("FizzBuzz")
  elif loop%3==0:
    print("Fizz")
  elif loop%5==0:
    print("Buzz")
  else:
    print loop
print "\n"
