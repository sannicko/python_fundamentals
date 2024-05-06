import random 

def roll_dice():
  dice_total = random.randint(1, 6) + random.randint(1, 6)
  return dice_total

def main():
  player1 = input("Enter player one name: \n")
  player2 = input("Enter player two name: \n")

  roll1 = roll_dice()
  roll2 = roll_dice()
  
  print(player1, 'rolled', roll1)
  print(player2, 'rolled', roll2) 

  if roll1 > roll2:
    print("Player one wins", player1, roll1)
  elif roll2 > roll1:
    print("Player two wins", player2, roll2)
  else:
    print("Tie game")
main()

