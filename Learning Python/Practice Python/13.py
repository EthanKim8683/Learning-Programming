# Fibonacci

def fibonacci(n):
  numbers = []

  a, b = 1, 1
  for i in range(n):
    numbers.append(a)
    a, b = b, a + b
  
  return numbers

if __name__ == "__main__":
  n = int(input("Fibonacci count: "))

  print(fibonacci(n))