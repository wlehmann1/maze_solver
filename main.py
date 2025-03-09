import sys
from window import Window, Point, Line
from maze import Cell, Maze

def main():
    sys.setrecursionlimit(10000)
    # Create window
    win = Window(800, 600)
    # Test drawing some cells
    maze = Maze(10, 10, 5, 7, 50, 50, win, 10)
    print("Maze created")
    is_solvable = maze.solve()
    if not is_solvable:
        print("Maze cannot be solved")
    else:
        print("Maze solved!")
    # Wait for close
    win.wait_for_close()

main()