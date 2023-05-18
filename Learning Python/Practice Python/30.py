# Pick Word

import random

if __name__ == "__main__":
  words = []
  with open("30.txt", 'r') as f:
    while word:=f.readline():
      words.append(word.strip())

  print(words[random.randint(0, len(words) - 1)])