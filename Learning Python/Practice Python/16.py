# Password Generator

import random

domain = ""
def domain_add_range(lower, upper):
  global domain

  for i in range(ord(lower), ord(upper) + 1):
    domain += chr(i)

domain_add_range('a', 'z')
domain_add_range('A', 'Z')
domain_add_range('0', '9')
domain += "~!@#$%^&*()_+`-={}|[]\\;':\",./<>?"

def generate_password(length):
  password = ""

  for i in range(length):
    password += domain[random.randint(0, len(domain) - 1)]
  
  return password

if __name__ == "__main__":
  while True:
    length = input("Length (or `exit` to exit): ").lower()

    if length == "exit":
      break
      
    print(generate_password(int(length)))