from graphics import Window, Line, Point
from maze import Maze
from cell import Cell

def main():
    win = Window(800, 600)
    maze = Maze(50, 50, 15, 15, 20, 20, win)
    maze.solve()
    win.wait_for_close()



if __name__ == "__main__": 
    main()