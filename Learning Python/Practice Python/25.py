# Guessing Game Two

class GuessingStrategy:
  TOO_HIGH = 0
  TOO_LOW = 1

  def __init__(self):
    self.l = 0
    self.r = 100

  def guess(self):
    return self.l + (self.r - self.l) // 2
  
  def update(self, feedback):
    if feedback == GuessingStrategy.TOO_HIGH:
      self.r = self.guess() - 1

    elif feedback == GuessingStrategy.TOO_LOW:
      self.l = self.guess() + 1

if __name__ == "__main__":
  playing = True
  while playing:
    guesser = GuessingStrategy()

    guessing = True
    while guessing:
      feedback = input(f"Is {guesser.guess()} >, < or = to your number (or `exit` to exit)? ").strip().lower()

      if feedback == "exit":
        guessing = False
        break

      if feedback == '>':
        guesser.update(GuessingStrategy.TOO_HIGH)
      
      elif feedback == '<':
        guesser.update(GuessingStrategy.TOO_LOW)

      elif feedback == '=':
        guessing = False
    
    deciding = True
    while deciding:
      decision = input("Play again (Y/n): ").strip().lower()

      if decision == 'y':
        deciding = False
      
      elif decision == 'n':
        deciding = False
        playing = False