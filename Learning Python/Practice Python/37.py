# Functions Refactor

def draw_board(width, height):
  def draw_horizontal():
    print(' ' + "--- " * width)

  def draw_vertical():
    print('|' + "   |" * width)

  draw_horizontal()
  for i in range(height):
    draw_vertical()
    draw_horizontal()

if __name__ == "__main__":
  draw_board(3, 3)