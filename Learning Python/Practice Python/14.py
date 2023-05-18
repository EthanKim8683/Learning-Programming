# List Remove Duplicates

import random

EXTRA = 0

def loop_unique(input_list):
  result = []

  for x in input_list:
    if x not in result:
      result.append(x)

  return result

def set_unique(input_list):
  return list(set(input_list))

def exercise_5_random_list():
  return [random.randint(1, 100) for i in range(random.randint(10, 20))]

def exercise_5_list_overlap(a, b):
  return list(set(a).intersection(set(b)))

if __name__ == "__main__":
  if EXTRA == 0:
    names = ["Michele", "Robin", "Sara", "Michele"]

    print("loop_unique: " + str(loop_unique(names)))

  elif EXTRA == 1:
    names = ["Michele", "Robin", "Sara", "Michele"]

    print("loop_unique: " + str(loop_unique(names)))
    print("set_unique: " + str(set_unique(names)))

  elif EXTRA == 2:
    a = exercise_5_random_list()
    b = exercise_5_random_list()
    c = exercise_5_list_overlap(a, b)

    print("a: " + str(a))
    print("b: " + str(b))
    print("c: " + str(c))