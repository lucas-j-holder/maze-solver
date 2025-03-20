from drawables import Cell
from window import Window
from time import sleep
import random
class Maze():

  def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window:Window=None, seed=None):
    self.x1 = x1
    self.y1 = y1
    self.num_rows = num_rows
    self.num_cols = num_cols
    self.cell_size_x = cell_size_x
    self.cell_size_y = cell_size_y
    self.window = window
    self._cells = []
    self._create_cells()
    random.seed(seed)
    self._break_entrance_and_exit()
    self._break_walls_r(0, 0)
    self._reset_cells_visited()
  
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
  
  def _reset_cells_visited(self):
     for i in range(len(self._cells)):
        for j in range(len(self._cells[i])):
           self._cells[i][j].visited = False

  def _break_walls_r(self, i, j):
    cell = self._cells[i][j]
    cell.visited = True
    while True:
      to_visit = []
      if i > 0 and not self._cells[i-1][j].visited:
          to_visit.append({"direction": "up", "position": [i-1, j]})
      if j > 0 and not self._cells[i][j-1].visited:
          to_visit.append({"direction": "left", "position": [i, j-1]})
      if i < len(self._cells)-1 and not self._cells[i+1][j].visited:
          to_visit.append({"direction": "down", "position": [i+1, j]})
      if j < len(self._cells[0])-1 and not self._cells[i][j+1].visited:
          to_visit.append({"direction": "right", "position": [i, j+1]})
      if len(to_visit) == 0:
         self._draw_cell(i,j)
         return
      
      rand_num = random.randrange(0, len(to_visit))
      random_direction, random_position  = to_visit[rand_num]["direction"], to_visit[rand_num]["position"]

      to_cell = self._cells[random_position[0]][random_position[1]]

      match random_direction:
          case "up":
            to_cell.bottom_wall = False
            cell.top_wall = False
          case "left":
            to_cell.right_wall = False
            cell.left_wall = False
          case "down":
            to_cell.top_wall = False
            cell.bottom_wall = False
          case "right":
            to_cell.left_wall = False
            cell.right_wall = False
      
      self._break_walls_r(random_position[0], random_position[1])

  def solve(self):
    return self._solve_r(0, 0)

  def _solve_r(self, i, j):
    cell = self._cells[i][j]
    end_cell = self._cells[-1][-1]
    self._animate()
    cell.visited = True
    if cell == end_cell:
       return True
    to_visit = []
    if i > 0 and not self._cells[i-1][j].visited and not cell.top_wall:
        to_visit.append({"direction": "up", "position": [i-1, j]})
    if j > 0 and not self._cells[i][j-1].visited and not cell.left_wall:
        to_visit.append({"direction": "left", "position": [i, j-1]})
    if i < len(self._cells)-1 and not self._cells[i+1][j].visited and not cell.bottom_wall:
        to_visit.append({"direction": "down", "position": [i+1, j]})
    if j < len(self._cells[0])-1 and not self._cells[i][j+1].visited and not cell.right_wall:
        to_visit.append({"direction": "right", "position": [i, j+1]})
    
    for direction in to_visit:
      position = direction["position"]
      cell.draw_move(self._cells[position[0]][position[1]])
      result = self._solve_r(position[0], position[1])
      if result:
         return True
      else:
         cell.draw_move(self._cells[position[0]][position[1]], True)
    return False
       
    

    
