# f Strings

import datetime

if __name__ == "__main__":
  year = datetime.date.today().year

  name = input("Name: ")
  age = int(input("Age: "))
  
  print(f"You, {name}, will turn 100 years old in {year + 100 - age}!")