from window import Window, Point, Line
from maze import Cell, Maze

def main():
    # Create window
    win = Window(800, 600)
    
    # Test drawing some cells
    maze = Maze(10, 10, 5, 7, 50, 50, win)
    
    # Wait for close
    win.wait_for_close()

main()