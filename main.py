from window import Window, Point, Line
from maze import Cell

def main():
    # Create window
    win = Window(800, 600)
    
    # Test drawing some cells
    c = Cell(win)
    c.has_right_wall = False
    c.draw(50, 50, 100, 100)

    d = Cell(win)
    d.has_left_wall = False
    d.draw(100, 50, 150, 100)

    c.draw_move(d)
    
    # Wait for close
    win.wait_for_close()

main()