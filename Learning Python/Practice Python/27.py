# Tic Tac Toe Draw

import re

class TicTacToe:
  X = 1
  O = 2
  PLAYERS = [X, O]
  SYMBOLS = [' ', 'X', '0']

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

  def get_board_string(self):
    result = " ---" * 3 + '\n'

    for i in range(3):
      result += '|'
      for j in range(3):
        result += f" {TicTacToe.SYMBOLS[self.board[i][j]]} |"

      result += '\n' + " ---" * 3 + '\n'

    return result.strip()

  def play_move(self, row, column):
    if row >= 3 or column >= 3:
      return False
    
    if self.board[row][column] != 0:
      return False
    
    self.board[row][column] = TicTacToe.PLAYERS[self.player]
    self.player = (self.player + 1) % len(TicTacToe.PLAYERS)

    return True
  
if __name__ == "__main__":
  tic_tac_toe = TicTacToe()

  while True:
    user_input = input("Row, column: ").strip()
    user_coordinates = re.search(r"^([0-2]),? ([0-2])$", user_input)

    if user_coordinates == None:
      continue

    row, column = int(user_coordinates.group(1)), int(user_coordinates.group(2))
    
    if tic_tac_toe.play_move(row, column):
      print(tic_tac_toe.get_board_string())