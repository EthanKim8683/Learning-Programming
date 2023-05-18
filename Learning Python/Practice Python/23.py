# File Overlap

def get_numbers_from_file(filename):
  numbers = []

  with open(filename, 'r') as f:
    while number:=f.readline():
      numbers.append(int(number))
  
  return numbers

def get_overlap(list1, list2):
  return list(set(list1).intersection(set(list2)))

if __name__ == "__main__":
  prime_numbers = get_numbers_from_file("23a.txt")
  happy_numbers = get_numbers_from_file("23b.txt")
  overlap = get_overlap(prime_numbers, happy_numbers)

  print(overlap)