# Max Of Three

import random

def max2(a, b):
  return a if a > b else b

def max3(a, b, c):
  return max2(max2(a, b), c)

if __name__ == "__main__":
  a = random.randint(1, 100)
  b = random.randint(1, 100)
  c = random.randint(1, 100)

  print("a: " + str(a))
  print("b: " + str(b))
  print("c: " + str(c))
  print("max3(a, b, c): " + str(max3(a, b, c)))