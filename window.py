from tkinter import Tk, BOTH, Canvas
from drawables import Line

class Window():
  def __init__(self, width, height):
    self.__root = Tk()

    self.__root.title("Maze Solver")
    self.__root.protocol("WM_DELETE_WINDOW", self.close)

    self.canvas = Canvas(width=width,height=height)

    self.canvas.pack()
    self.running = False

  def redraw(self):
    self.__root.update_idletasks()
    self.__root.update()
  
  def draw_line(self, line:Line, fill_color):
    line.draw(self.canvas, fill_color)
  
  def wait_for_close(self):
    self.running = True
    while self.running:
      self.redraw()
  
  def close(self):
    self.running = False
    
