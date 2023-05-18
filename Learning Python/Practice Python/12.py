# List Ends

def list_ends(x):
  return [x[0], x[-1]]

if __name__ == "__main__":
  a = [5, 10, 15, 20, 25]

  print(list_ends(a))