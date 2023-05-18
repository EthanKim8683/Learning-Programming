# Element Search

import random

EXTRA = 1

def random_ordered_list(length=10):
  result = [random.randint(1, 20) for i in range(length)]
  result.sort()
  return result

def complete_search(haystack, needle):
  return needle in haystack

def binary_search(haystack, needle):
  l, r = 0, len(haystack) - 1
  while l <= r:
    m = l + (r - l) // 2
    if haystack[m] > needle:
      r = m - 1
    elif haystack[m] < needle:
      l = m + 1
    else:
      return True
  return False

if __name__ == "__main__":
  haystack = random_ordered_list()
  needle = random.randint(1, 20)

  print("Haystack: " + str(haystack))
  print("Needle: " + str(needle))

  if EXTRA == 0:
    print("Needle in haystack: " + str(complete_search(haystack, needle)))
  
  elif EXTRA == 1:
    print("Needle in haystack: " + str(binary_search(haystack, needle)))