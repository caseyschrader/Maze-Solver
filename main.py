from graphics import Window, Line, Point, Cell

def main():
    win = Window(800, 600)
    cell1 = Cell(50, 100, 50, 100, win)
    cell2 = Cell(150, 200, 150, 100, win)

    cell1.draw()
    cell2.draw()

    cell1.draw_move(cell2)
    win.wait_for_close()



if __name__ == "__main__": 
    main()