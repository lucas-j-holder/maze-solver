from drawables import Cell
from window import Window
from drawables import Cell
from time import sleep
class Maze():

  def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window:Window):
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
        self._draw_cell(row_num, col_num)
    
  def _draw_cell(self, i, j):
    self._cells[i][j].draw()
    self._animate()
  
  def _animate(self):
    self.window.redraw()
    sleep(0.05)
