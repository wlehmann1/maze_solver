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
    
    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self._win:
            if self.has_left_wall:
                line = Line(Point(x1, y1), Point(x1, y2))
                self._win.draw_line(line, "black")
            else:
                line = Line(Point(x1, y1), Point(x1, y2))
                self._win.draw_line(line, "white")
            if self.has_top_wall:
                line = Line(Point(x1, y1), Point(x2, y1))
                self._win.draw_line(line, "black")
            else:
                line = Line(Point(x1, y1), Point(x2, y1))
                self._win.draw_line(line, "white")
            if self.has_right_wall:
                line = Line(Point(x2, y1), Point(x2, y2))
                self._win.draw_line(line, "black")
            else:
                line = Line(Point(x2, y1), Point(x2, y2))
                self._win.draw_line(line, "white")
            if self.has_bottom_wall:
                line = Line(Point(x1, y2), Point(x2, y2))
                self._win.draw_line(line, "black")
            else:
                line = Line(Point(x1, y2), Point(x2, y2))
                self._win.draw_line(line, "white")
    
    def draw_move(self, to_cell, undo=False):
        if self._win:
            if undo == False:
                color = "red"
            else:
                color = "gray"
            line = Line(Point((self._x1+self._x2)/2,(self._y1+self._y2)/2), Point((to_cell._x1+to_cell._x2)/2,(to_cell._y1+to_cell._y2)/2))
            self._win.draw_line(line, color)

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window=None):
        self.win = window
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._cells = []
        self._create_cells()
    
    def _create_cells(self):
        for g in range(self.num_cols):
            column = []
            for h in range(self.num_rows):
                column.append(Cell(self.win))
            self._cells.append(column)
        self._break_entrance_and_exit()
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
        #self._draw_cell(0, 0)
        self._cells[-1][-1].has_bottom_wall = False
        #self._draw_cell(self.num_rows, self.num_cols)