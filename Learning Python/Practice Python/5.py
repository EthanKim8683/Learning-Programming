# List Overlap

import random

EXTRA = 0

if __name__ == "__main__":
  if EXTRA == 0:
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    a.sort()
    b.sort()

    c = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
      if a[i] < b[j]:
        i += 1
      elif a[i] > b[j]:
        j += 1
      else:
        c.append(a[i])
        i += 1
        j += 1
  
  elif EXTRA == 1:
    a = [random.randint(1, 100) for i in range(random.randint(10, 20))]
    b = [random.randint(1, 100) for i in range(random.randint(10, 20))]

    c = []
    for key in a:
      if key in b:
        c.append(key)
  
  elif EXTRA == 2:
    a = [random.randint(1, 100) for i in range(random.randint(10, 20))]
    b = [random.randint(1, 100) for i in range(random.randint(10, 20))]

    c = list(filter(lambda x: x in b, a))
    
  print("a: " + str(a))
  print("b: " + str(b))
  print("c: " + str(c))