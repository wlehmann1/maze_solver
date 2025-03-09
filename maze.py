import random
import time
from window import Point, Line

class Cell():
    def __init__(self, window=None):
        self._win = window
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
    
    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self._win:
            black_color = "black"
            bg_color = "#D9D9D9"
            if self.has_left_wall:
                line = Line(Point(x1, y1), Point(x1, y2))
                self._win.draw_line(line, black_color)
            else:
                line = Line(Point(x1, y1), Point(x1, y2))
                self._win.draw_line(line, bg_color)
            if self.has_top_wall:
                line = Line(Point(x1, y1), Point(x2, y1))
                self._win.draw_line(line, black_color)
            else:
                line = Line(Point(x1, y1), Point(x2, y1))
                self._win.draw_line(line, bg_color)
            if self.has_right_wall:
                line = Line(Point(x2, y1), Point(x2, y2))
                self._win.draw_line(line, black_color)
            else:
                line = Line(Point(x2, y1), Point(x2, y2))
                self._win.draw_line(line, bg_color)
            if self.has_bottom_wall:
                line = Line(Point(x1, y2), Point(x2, y2))
                self._win.draw_line(line, black_color)
            else:
                line = Line(Point(x1, y2), Point(x2, y2))
                self._win.draw_line(line, bg_color)
    
    def draw_move(self, to_cell, undo=False):
        if self._win:
            if undo == False:
                color = "red"
            else:
                color = "gray"
            line = Line(Point((self._x1+self._x2)/2,(self._y1+self._y2)/2), Point((to_cell._x1+to_cell._x2)/2,(to_cell._y1+to_cell._y2)/2))
            self._win.draw_line(line, color)

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window=None, seed=None):
        self.win = window
        self.seed = random.seed(seed)
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
    
    def _create_cells(self):
        for g in range(self.num_cols):
            column = []
            for h in range(self.num_rows):
                column.append(Cell(self.win))
            self._cells.append(column)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        x1 = (i * self.cell_size_x) + self.x1
        y1 = (j * self.cell_size_y) + self.y1
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self.win:
            self.win.redraw()
            time.sleep(0.05)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)
    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            next_index_list = []
            # Determine nearby cells that can be visited
            if i > 0 and not self._cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
            if i < self.num_cols - 1 and not self._cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))
            if j > 0 and not self._cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
            if j < self.num_rows - 1 and not self._cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))
            # If nowhere to go, stop loop
            if len(next_index_list) == 0:
                self._draw_cell(i, j)
                return
            # Randomly choose a direction
            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]
            # Knock out walls
            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False
            # Visit next cell
            self._break_walls_r(next_index[0], next_index[1])
    
    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False
    
    def _solve_r(self, i, j):
        self._animate()
        # Vist the cell passed to us
        self._cells[i][j].visited = True
        # Done if at maze exit
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        # Move left if there is no wall and it hasn't been visited
        if (
            i > 0
            and not self._cells[i][j].has_left_wall
            and not self._cells[i - 1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)
        # Move right if there is no wall and it hasn't been visited
        if (
            i < self.num_cols - 1
            and not self._cells[i][j].has_right_wall
            and not self._cells[i + 1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)
        # Move up if there is no wall and it hasn't been visited
        if (
            j > 0
            and not self._cells[i][j].has_top_wall
            and not self._cells[i][j - 1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)
        # Move down if there is no wall and it hasn't been visited
        if (
            j < self.num_rows - 1
            and not self._cells[i][j].has_bottom_wall
            and not self._cells[i][j + 1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)
        # No other options
        return False

    def solve(self):
        return self._solve_r(0, 0)