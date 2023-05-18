# Pick Word

import random
import re

class Hangman:
  words = None

  def __init__(self):
    if Hangman.words == None:
      Hangman.words = []
      with open("30.txt", 'r') as f:
        while word:=f.readline():
          Hangman.words.append(word.strip().lower())

    self.word = Hangman.__get_random_word()
    self.mask = ['_'] * len(self.word)
    self.guessed = set()

  def __get_random_word():
    return Hangman.words[random.randint(0, len(Hangman.words) - 1)]
  
  def guess_letter(self, letter):
    if letter in self.guessed:
      return None
    self.guessed.add(letter)

    updates = 0
    for i in range(len(self.word)):
      if letter == self.word[i]:
        self.mask[i] = letter
        updates += 1

    if updates == 0:
      return False
    
    return True
  
  def get_mask_string(self):
    return ' '.join(self.mask).upper()

if __name__ == "__main__":
  hangman = Hangman()

  while True:
    guess = input("Guess (or `exit` to exit): ").strip().lower()

    if guess == "exit":
      break

    if re.search(r"^\w$", guess) == None:
      continue

    result = hangman.guess_letter(guess)
    if result == True:
      print(hangman.get_mask_string())
    
    elif result == False:
      print("Incorrect!")