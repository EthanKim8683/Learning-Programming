# Error Checking

import random
import re

LOWER_BOUND = 1
UPPER_BOUND = 100

int_pattern = re.compile("^[+-]?[0-9]+$")

if __name__ == "__main__":
  exited = False
  while not exited:
    target = random.randint(LOWER_BOUND, UPPER_BOUND)

    guesses, guessing = 0, True
    while guessing and not exited:
      guess = input(f"Guess, in range [{LOWER_BOUND}, {UPPER_BOUND}] (or `exit` to exit): ").strip().lower()

      if guess == "exit":
        exited = True
        break
      
      if int_pattern.search(guess) == None:
        print("Invalid input!")
        continue

      guess = int(guess)
      guesses += 1

      if guess > target:
        print("Too high!")
      
      elif guess < target:
        print("Too low!")
      
      else:
        print(f"You guessed it in {guesses} tries!")
        guessing = False
    
    deciding = True
    while deciding:
      decision = input("Play again (Y/n)? ").strip().lower()

      if decision == 'y':
        deciding = False
      
      elif decision == 'n':
        deciding = False
        exited = True