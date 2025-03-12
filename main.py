from window import Window
from drawables import Point, Line, Cell
win = Window(800, 600)
point1 = Point(10,10)
point2 = Point(100,100)
line = Line(point1, point2)
win.draw_line(line, "#FF007F")

cell1 = Cell(10, 20, 10, 20, win).draw()
cell2 = Cell(100, 300, 100, 300, win).draw("#FF007F")
cell3 = Cell(500, 600, 200, 500, win).draw("#00FF00")

cell2.draw_move(cell3)

win.wait_for_close()