# Odd Or Even

EXTRA = 2

if __name__ == "__main__":
  if EXTRA == 0:
    number = int(input("Number: "))

    if number % 2 == 0:
      print(f"{number} is even!")
    else:
      print(f"{number} is odd!")
    
  elif EXTRA == 1:
    number = int(input("Number: "))

    if number % 2 == 0:
      print(f"{number} is even", end="")
    else:
      print(f"{number} is odd", end="")
    
    if number % 4 == 0:
      print(" and a multiple of 4", end="")
    
    print("!")
  
  elif EXTRA == 2:
    number = int(input("Number: "))
    check = int(input("Check: "))

    if number % check == 0:
      print(f"{number} is divisible by {check}!")
    else:
      print(f"{number} is not divisible by {check}!")