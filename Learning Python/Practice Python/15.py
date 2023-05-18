# Reverse Word Order

def reverse(sentence):
  return " ".join(sentence.split(" ")[::-1])

if __name__ == "__main__":
  sentence = input("Sentence: ")

  print(reverse(sentence))