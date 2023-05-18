# List Comprehensions

if __name__ == "__main__":
  a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
  
  # print(list(filter(lambda x: x % 2 == 0, a)))
  print([x for x in a if x % 2 == 0])