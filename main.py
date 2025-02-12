from graphics import Window, Line, Point, Cell, Maze

def main():
    win = Window(800, 600)
    maze = Maze(50, 50, 10, 10, 20, 20, win)
    win.wait_for_close()



if __name__ == "__main__": 
    main()