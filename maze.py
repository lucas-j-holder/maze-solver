from drawables import Cell
from window import Window
from time import sleep
class Maze():

  def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window:Window=None):
    self.x1 = x1
    self.y1 = y1
    self.num_rows = num_rows
    self.num_cols = num_cols
    self.cell_size_x = cell_size_x
    self.cell_size_y = cell_size_y
    self.window = window
    self._cells = []
    self._create_cells()
  
  def _create_cells(self):
    
    for row_num in range(self.num_rows):
      self._cells.append([])
      x1 = self.x1
      y1 = self.y1 + self.cell_size_y * row_num
      row = self._cells[row_num]
      for col_num in range(self.num_cols):
        x1 = x1 + self.cell_size_x
        row.append(Cell(x1, x1 + self.cell_size_x, y1, y1 + self.cell_size_y, self.window))
        if self.window is not None:
          self._draw_cell(row_num, col_num)
    
  def _draw_cell(self, i, j):
    if self.window is None:
      return
    self._cells[i][j].draw()
    self._animate()
  
  def _animate(self):
    self.window.redraw()
    sleep(0.05)

  def _break_entrance_and_exit(self):
    top_left_cell = self._cells[0][0]
    bottom_right_cell = self._cells[-1][-1]
    top_left_cell.top_wall = False
    self._draw_cell(0, 0)
    bottom_right_cell.bottom_wall = False
    self._draw_cell(-1, -1)