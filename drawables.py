from tkinter import Canvas
class Point():
  def __init__(self,x,y):
    self.x = x
    self.y = y

class Line():
  def __init__(self, point1, point2):
    self.point1 = point1
    self.point2 = point2

  def draw(self, canvas:Canvas, fill_color):
    canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2)

class Cell():
  def __init__(self, x1, x2, y1, y2, window=None):
    self.left_wall = True
    self.top_wall = True
    self.right_wall = True
    self.bottom_wall = True
    self._x1 = x1
    self._x2 = x2
    self._y1 = y1
    self._y2 = y2
    self.win = window
  
  def draw(self, draw_color="#000000"):
    point_top_left = Point(self._x1, self._y1)
    point_bottom_left = Point(self._x1, self._y2)
    point_top_right = Point(self._x2, self._y1)
    point_bottom_right = Point(self._x2, self._y2)


    # For each wall, check if the wall should be present, if it is, then draw a wall of the draw_color, else white.
    self.win.draw_line(Line(point_top_left, point_top_right), draw_color if self.top_wall else "white")
    self.win.draw_line(Line(point_top_left, point_bottom_left),draw_color if self.left_wall else "white")
    self.win.draw_line(Line(point_top_right, point_bottom_right),draw_color if self.right_wall else "white")
    self.win.draw_line(Line(point_bottom_left, point_bottom_right), draw_color if self.bottom_wall else "white")
    return self
  
  def draw_move(self, to_cell, undo=False):

    def get_middle(cell):
      return Point(((cell._x1 + cell._x2) / 2), ((cell._y1 + cell._y2) / 2))
    
    point1 = get_middle(self)
    point2 = get_middle(to_cell)
    color = "gray" if undo else "red"
    line = Line(point1, point2)
    self.win.draw_line(line, color)