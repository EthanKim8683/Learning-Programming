# Read From File

import re

EXTRA = 1

if __name__ == "__main__":
  if EXTRA == 0:
    counts = {}

    with open("22a.txt", 'r') as f:
      while key:=f.readline():
        key = key.strip()
        if key not in counts.keys():
          counts[key] = 0
        counts[key] += 1
    
    for key, value in counts.items():
      print(str(key) + ": " + str(value))

  elif EXTRA == 1:
    counts = {}

    with open("22b.txt", 'r') as f:
      while key:=f.readline():
        key = re.search(r"(?<=/./).+(?=/.+\.jpg)", key)
        if key == None:
          continue
        key = key.group()

        if key not in counts.keys():
          counts[key] = 0
        counts[key] += 1
    
    for key, value in counts.items():
      print(str(key) + ": " + str(value))