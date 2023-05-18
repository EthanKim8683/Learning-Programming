# Check Primality Functions

SIEVE_SIZE = 100000

class LinearSieve:
  def __init__(self, size=SIEVE_SIZE):
    self.sieve = [0] * size
    self.size = size

    for i in range(2, size):
      if self.sieve[i] == 0:
        self.sieve[i] = i
        for j in range(i * i, size, i):
          if self.sieve[j] == 0:
            self.sieve[j] = i
  
  def factorize(self, x):
    factors = []

    while x != 1:
      factor = self.sieve[x]
      factors.append(factor)

      x //= factor
    
    return factors

if __name__ == "__main__":
  linear_sieve = LinearSieve()

  dividend = int(input(f"Dividend, in range [1, {linear_sieve.size}): "))
  
  print(linear_sieve.factorize(dividend))
  