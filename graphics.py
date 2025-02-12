from tkinter import Tk, BOTH, Canvas

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

class Cell:
    def __init__(self, x1, x2, y1, y2,win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

        self.__win = win

    def draw(self):
        if self.has_left_wall == True:
          # print("Drawing left wall")
            start = Point(self.__x1, self.__y1)
            end = Point(self.__x1, self.__y2)
            line = Line(start,end)
            self.__win.draw_line(line)

        if self.has_right_wall == True:
          # print("Drawing right wall")
            start = Point(self.__x2, self.__y1)
            end = Point(self.__x2, self.__y2)
            line = Line(start,end)
            self.__win.draw_line(line)
# coordinate system is flipped in tkinter, y2 is bottom not top.
        if self.has_top_wall == True:
          # print("Drawing top wall")
            start = Point(self.__x1, self.__y1)
            end = Point(self.__x2, self.__y1)
            line = Line(start, end)
            self.__win.draw_line(line)

        if self.has_bottom_wall == True:
          # print("Drawing bottom wall")
            start = Point(self.__x1, self.__y2)
            end = Point(self.__x2, self.__y2)
            line = Line(start,end)
            self.__win.draw_line(line)

    def draw_move(self, to_cell, undo=False):
        from_midpoint = Point((self.__x1 + self.__x2)/2, (self.__y1 +self.__y2)/2)
        to_midpoint = Point((to_cell.__x1 + to_cell.__x2)/2, (to_cell.__y1 + to_cell.__y2)/2)
        line = Line(from_midpoint, to_midpoint)
        if undo == False:
            self.__win.draw_line(line, fill_color="red")
        else:
            self.__win.draw_line(line, fill_color="gray")




        
    










