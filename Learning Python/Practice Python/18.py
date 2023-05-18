# Cows And Bulls

import random
import re

guess_pattern = re.compile("[0-9]{4}")

class CowsAndBulls:
  def __init__(self):
    self.target = ""
    for i in range(4):
      self.target += str(random.randint(0, 9))

  def count_cows(self, guess):
    cows = 0

    for i in range(4):
      if guess[i] == self.target[i]:
        cows += 1
    
    return cows
  
  def count_bulls(self, guess):
    bulls = 0

    guess_remaining = set()
    target_remaining = set()
    for i in range(4):
      if guess[i] != self.target[i]:
        guess_remaining.add(guess[i])
        target_remaining.add(self.target[i])

    return len(guess_remaining.intersection(target_remaining))

if __name__ == "__main__":
  playing = True
  while playing:
    cows_and_bulls = CowsAndBulls()

    guessing = True
    while guessing:
      guess = input("Guess (or `exit` to exit): ").strip().lower()

      if guess == "exit":
        guessing = False
        break
      
      if len(guess) != 4 or guess_pattern.search(guess) == None:
        continue

      cows = cows_and_bulls.count_cows(guess)
      bulls = cows_and_bulls.count_bulls(guess)

      print("Cows: ", cows)
      print("Bulls: ", bulls)

      if cows == 4:
        break
    
    deciding = True
    while deciding:
      decision = input("Play again (Y/n): ").strip().lower()

      if decision == 'y':
        deciding = False
      
      elif decision == 'n':
        deciding = False
        playing = False