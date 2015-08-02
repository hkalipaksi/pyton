from random import randint

def enemy():
  rand=randint(1,3)
  if rand==1:
    return "rock"
  elif rand==2:
    return "scissors"
  elif rand==3:
    return "paper"
 


def suit(player,enemy):
    if player==enemy:
        return "draw"
    if player=="scissors":
        if enemy=="paper":
          return "you win"
        elif  enemy =="rock":
          return "you lose"
    elif player=="paper":
        if enemy=="rock":
          return "you win"
        elif enemy=="scissors":
          return "you lose"

def main_program():
  player=raw_input("what is your choice (rock/paper/scissors):")
  print suit(player,enemy())

main_program()
