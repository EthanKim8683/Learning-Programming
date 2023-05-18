# List Overlap Comprehensions

import random

EXTRA = 1

if __name__ == "__main__":
  if EXTRA == 0:
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

  elif EXTRA == 1:
    a = [random.randint(1, 100) for i in range(random.randint(10, 20))]
    b = [random.randint(1, 100) for i in range(random.randint(10, 20))]

  print("a: " + str(a))
  print("b: " + str(b))
  print("c: " + str([x for x in a if x in b]))