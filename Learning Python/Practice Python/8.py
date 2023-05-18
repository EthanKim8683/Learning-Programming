# Rock Paper Scissors

import random

def to_string(char):
  if char == 'r':
    return "Rock"
  
  if char == 'p':
    return "Paper"
  
  if char == 's':
    return "Scissors"
  
  return "Invalid option"

def win(a, b):
  return (a == 'r' and b == 's') or (a == 'p' and b == 'r') or (a == 's' and b == 'p')

def draw(a, b):
  return a == b

def lose(a, b):
  return not win(a, b) and not draw(a, b)

if __name__ == "__main__":
  player_score, opponent_score = 0, 0

  while True:
    player = input("Rock:\t\tR/r\nPaper:\t\tP/p\nScissors:\tS/s\nQuit:\t\tQ/q\n").strip().lower()

    if player in "rps":
      opponent = "rps"[random.randint(0, 2)]
      print(f"Your opponent chooses `{to_string(opponent)}`!")

      if win(player, opponent):
        print(f"`{to_string(player)}` beats `{to_string(opponent)}`, you win!")
        player_score += 1

      elif draw(player, opponent):
        print(f"`{to_string(player)}` draws `{to_string(opponent)}`, you draw.")

      elif lose(player, opponent):
        print(f"`{to_string(opponent)}` beats `{to_string(player)}`, you lose.")
        opponent_score += 1
      
      print(f"The current score is {player_score} to {opponent_score}.")

    elif player == 'q':
      break
      
    print()