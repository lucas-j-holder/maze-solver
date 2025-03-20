import unittest

from maze import Maze

class Tests(unittest.TestCase):
  def test_maze_create_cells(self):
    num_cols = 8
    num_rows = 6
    m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

    self.assertEqual(len(m1._cells), num_rows)
    self.assertEqual(len(m1._cells[0]), num_cols)

  def test_maze_break_entrace(self):
    num_cols = 8
    num_rows = 6
    m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

    m1._break_entrance_and_exit()

    top_left = m1._cells[0][0]
    bottom_right = m1._cells[-1][-1]
    self.assertEqual(top_left.top_wall, False)
    self.assertEqual(bottom_right.bottom_wall, False)

if __name__ == "__main__":
  unittest.main()
  
