# Tic Tac Toe Game

import re

class TicTacToeAPI:
  X = 1
  O = 2
  PLAYERS = [X, O]
  SYMBOLS = [' ', 'X', 'O']

  def __init__(self):
    self.board = [[0] * 3 for i in range(3)]
    self.player = 0
  
  def __get_winner_major_diagonal(self):
    for i in range(3):
      if self.board[i][i] != self.board[0][0]:
        return 0
      
    return self.board[0][0]
  
  def __get_winner_minor_diagonal(self):
    for i in range(3):
      if self.board[i][2 - i] != self.board[0][2]:
        return 0
      
    return self.board[0][2]
  
  def __get_winner_row(self, row):
    for i in range(3):
      if self.board[row][i] != self.board[row][0]:
        return 0
      
    return self.board[row][0]
  
  def __get_winner_column(self, column):
    for i in range(3):
      if self.board[i][column] != self.board[0][column]:
        return 0
      
    return self.board[0][column]

  def get_winner(self):
    if (winner:=self.__get_winner_major_diagonal()) != 0:
      return winner
    
    if (winner:=self.__get_winner_minor_diagonal()) != 0:
      return winner
    
    for i in range(3):
      if (winner:=self.__get_winner_row(i)) != 0:
        return winner
      
    for i in range(3):
      if (winner:=self.__get_winner_column(i)) != 0:
        return winner
      
    return 0
  
  def is_over(self):
    if self.get_winner() != 0:
      return True
    
    for i in range(3):
      for j in range(3):
        if self.board[i][j] == 0:
          return False
        
    return True

  def get_board_string(self):
    result = " ---" * 3 + '\n'

    for i in range(3):
      result += '|'
      for j in range(3):
        result += f" {TicTacToeAPI.SYMBOLS[self.board[i][j]]} |"

      result += '\n' + " ---" * 3 + '\n'

    return result.strip()

  def play_move(self, row, column):
    if row >= 3 or column >= 3:
      return False
    
    if self.board[row][column] != 0:
      return False
    
    self.board[row][column] = TicTacToeAPI.PLAYERS[self.player]
    self.player = (self.player + 1) % len(TicTacToeAPI.PLAYERS)

    return True
  
class TicTacToeGame:
  def __init__(self):
    self.api = TicTacToeAPI()

  def __get_input():
    user_input = input("Row, column: ").strip()
    user_coordinates = re.search(r"^([0-2]),? ([0-2])$", user_input)

    if user_coordinates == None:
      return None
    
    return (int(user_coordinates.group(1)), int(user_coordinates.group(2)))
  
  def play(self):
    while True:
      player = TicTacToeAPI.SYMBOLS[TicTacToeAPI.PLAYERS[self.api.player]]
      print(f"Player `{player}`'s move!")

      move = TicTacToeGame.__get_input()
      if move == None:
        continue

      row, column = move
      self.api.play_move(row, column)
      print(self.api.get_board_string())

      print()

      if self.api.is_over():
        if (winner:=self.api.get_winner()) != 0:
          winner = TicTacToeAPI.SYMBOLS[winner]
          print(f"Player `{winner}` wins!")
          return winner
        
        else:
          print("Draw!")
          return None
  
if __name__ == "__main__":
  scores = {'X': 0, 'O': 0}

  playing = True
  while playing:
    game = TicTacToeGame()
    winner = game.play()
    if winner != None:
      scores[winner] += 1

    print()
    print(f"The current score is {scores['X']} to {scores['O']}.")
    print()
    
    deciding = True
    while deciding:
      decision = input("Play again (Y/n)? ").strip().lower()

      if decision == 'y':
        deciding = False
      
      elif decision == 'n':
        deciding = False
        playing = False

    print()