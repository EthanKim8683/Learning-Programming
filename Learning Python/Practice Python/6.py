# String Lists

if __name__ == "__main__":
  string = input("String: ")
  
  if string == string[::-1]:
    print(string + " is a palindrome")
  else:
    print(string + " is not a palindrome")