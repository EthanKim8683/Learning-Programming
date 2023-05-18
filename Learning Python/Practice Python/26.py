# Check Tic Tac Toe

class TicTacToe:
  def __init__(self):
    self.board = [[0] * 3] * 3
  
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

if __name__ == "__main__":
  winner_is_2 = [[2, 2, 0],
    [2, 1, 0],
    [2, 1, 1]]

  winner_is_1 = [[1, 2, 0],
    [2, 1, 0],
    [2, 1, 1]]

  winner_is_also_1 = [[0, 1, 0],
    [2, 1, 0],
    [2, 1, 1]]

  no_winner = [[1, 2, 0],
    [2, 1, 0],
    [2, 1, 2]]

  also_no_winner = [[1, 2, 0],
    [2, 1, 0],
    [2, 1, 0]]

  tic_tac_toe = TicTacToe()

  tic_tac_toe.board = winner_is_2
  print(tic_tac_toe.get_winner())
  
  tic_tac_toe.board = winner_is_1
  print(tic_tac_toe.get_winner())
  
  tic_tac_toe.board = winner_is_also_1
  print(tic_tac_toe.get_winner())
  
  tic_tac_toe.board = no_winner
  print(tic_tac_toe.get_winner())
  
  tic_tac_toe.board = also_no_winner
  print(tic_tac_toe.get_winner())