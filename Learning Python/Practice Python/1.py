# Character Input

import datetime

EXTRA = 0

if __name__ == "__main__":
  year = datetime.date.today().year

  name = input("Name: ")
  age = int(input("Age: "))
  
  message = f"You, {name}, will turn 100 years old in {year + 100 - age}!"

  if EXTRA == 0:
    print(message)

  elif EXTRA == 1:
    copies = int(input("# of copies: "))
    print(copies * message)

  elif EXTRA == 2:
    copies = int(input("# of copies: "))
    print(copies * (message + "\n"), end="")