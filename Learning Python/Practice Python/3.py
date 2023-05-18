# List Less Than Ten

EXTRA = 0

if __name__ == "__main__":
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

  if EXTRA == 0:
    a.sort()

    l, r = 0, len(a)
    while l < r:
      m = l + (r - l) // 2
      if a[m] < 5:
        l = m + 1
      else:
        r = m
    
    for i in range(l):
      print(a[i], end=" ")
    
  elif EXTRA == 1:
    b = []
    for i in a:
      if i < 5:
        b.append(i)

    print(b)
  
  elif EXTRA == 2:
    print(list(filter(lambda x: x < 5, a)))
  
  elif EXTRA == 3:
    threshold = int(input("Threshold: "))

    print(list(filter(lambda x: x < threshold, a)))