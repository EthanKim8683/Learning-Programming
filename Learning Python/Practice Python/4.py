# Divisors

SIEVE_SIZE = 100000

sieve = [0] * SIEVE_SIZE
for i in range(2, SIEVE_SIZE):
  if sieve[i] == 0:
    sieve[i] = i
    for j in range(i * i, SIEVE_SIZE, i):
      if sieve[j] == 0:
        sieve[j] = i

if __name__ == "__main__":
  dividend = int(input(f"Dividend, in range [1, {SIEVE_SIZE}): "))

  divisors = []
  while dividend != 1:
    divisor = sieve[dividend]
    dividend //= divisor
    divisors.append(divisor)
    
  print(divisors)

# if __name__ == "__main__":
#   dividend = int(input("Dividend: "))

#   divisors = []
#   i = 2
#   while i * i <= dividend:
#     while dividend % i == 0:
#       dividend //= i
#       divisors.append(i)
#     i += 1
#   if dividend != 1:
#     divisors.append(dividend)
  
#   print(divisors)