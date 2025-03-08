import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_maze_different_dimensions(self):
        # Test with different number of rows and columns
        num_cols = 5
        num_rows = 8
        m2 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m2._cells), num_cols)
        self.assertEqual(len(m2._cells[0]), num_rows)
    
    def test_maze_cell_sizes(self):
        # Test with different cell sizes
        num_cols = 7
        num_rows = 7
        cell_size_x = 20
        cell_size_y = 15
        m3 = Maze(0, 0, num_rows, num_cols, cell_size_x, cell_size_y)
        self.assertEqual(m3.cell_size_x, cell_size_x)
        self.assertEqual(m3.cell_size_y, cell_size_y)

if __name__ == "__main__":
    unittest.main()