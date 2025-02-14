from tkinter import Tk, BOTH, Canvas
import time

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", bd=1, height=height, width=width)
        self.__canvas.pack(expand=True, fill=BOTH)
        self.__window_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__window_running = True

        while self.__window_running == True:
            self.redraw()
    
    def close(self):
        self.__window_running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

class Point:
    def __init__(self,x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):

        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color):
        
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )