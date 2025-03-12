from window import Window
from drawables import Point, Line
win = Window(800, 600)
point1 = Point(10,10)
point2 = Point(100,100)
line = Line(point1, point2)
win.draw_line(line, "#FF007F")
win.wait_for_close()