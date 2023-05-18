# Hangman

import random
import re

class HangmanAPI:
  words = None

  def __init__(self):
    if HangmanAPI.words == None:
      HangmanAPI.words = []
      with open("30.txt", 'r') as f:
        while word:=f.readline():
          HangmanAPI.words.append(word.strip().lower())

    self.word = HangmanAPI.__get_random_word()
    self.mask = ['_'] * len(self.word)
    self.hangman = ['/', '\\', '/', '\\', '|', 'O']
    self.incorrect_count = 0
    self.correct_count = 0
    self.guessed = set()

  def __get_random_word():
    return HangmanAPI.words[random.randint(0, len(HangmanAPI.words) - 1)]
  
  def is_win(self):
    return self.correct_count == len(self.word)

  def is_over(self):
    if self.is_win():
      return True

    return self.incorrect_count == 6
  
  def guess_letter(self, letter):
    if letter in self.guessed:
      return None
    self.guessed.add(letter)

    updates = 0
    for i in range(len(self.word)):
      if letter == self.word[i]:
        self.mask[i] = letter
        self.correct_count += 1
        updates += 1

    if updates == 0:
      self.hangman[self.incorrect_count] = ' '
      self.incorrect_count += 1
      return False
    
    return True
  
  def get_mask_string(self):
    return ' '.join(self.mask).upper()
  
  def get_hangman_string(self):
    result = "  +---+\n"
    result += "  |   |\n"
    result += f"  |   {self.hangman[5]}\n"
    result += f"  |  {self.hangman[2]}{self.hangman[4]}{self.hangman[3]}\n"
    result += f"  |  {self.hangman[0]} {self.hangman[1]}\n"
    result += "  |\n"
    result += "========="
    return result

class HangmanGame:
  def __init__(self):
    self.api = HangmanAPI()

  def __get_input():
    guess = input("Guess your letter: ").strip().lower()

    if re.search(r"^[a-z]$", guess) == None:
      return None
    
    return guess
  
  def play(self):
    while True:
      user_input = HangmanGame.__get_input()
      if user_input == None:
        continue

      result = self.api.guess_letter(user_input)

      if result != None:
        print(self.api.get_hangman_string())
        print(self.api.get_mask_string())

      print()

      if self.api.is_over():
        if self.api.is_win():
          print("You win!")
          return True

        else:
          print("You lose!")
          print(f"The word was: {self.api.word.upper()}")
          return False

if __name__ == "__main__":
  playing = True
  while playing:
    game = HangmanGame()
    game.play()

    print()
    
    deciding = True
    while deciding:
      decision = input("Play again (Y/n)? ").strip().lower()

      if decision == 'y':
        deciding = False
      
      elif decision == 'n':
        deciding = False
        playing = False

    print()