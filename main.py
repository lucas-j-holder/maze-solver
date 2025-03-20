from window import Window
from drawables import Point, Line, Cell
from maze import Maze
win = Window(800, 600)
point1 = Point(10,10)
point2 = Point(100,100)
line = Line(point1, point2)

maze = Maze(100, 100, 10, 10, 20, 20, win)
maze._break_entrance_and_exit()

win.wait_for_close()