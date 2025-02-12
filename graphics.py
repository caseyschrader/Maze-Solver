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

class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None

        self.__win = win

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2



        if self.has_left_wall == True:
          # print("Drawing left wall")
            start = Point(x1, y1)
            end = Point(x1, y2)
            line = Line(start,end)
            self.__win.draw_line(line)

        if self.has_right_wall == True:
          # print("Drawing right wall")
            start = Point(x2, y1)
            end = Point(x2, y2)
            line = Line(start,end)
            self.__win.draw_line(line)
# coordinate system is flipped in tkinter, y2 is bottom not top.
        if self.has_top_wall == True:
          # print("Drawing top wall")
            start = Point(x1, y1)
            end = Point(x2, y1)
            line = Line(start, end)
            self.__win.draw_line(line)

        if self.has_bottom_wall == True:
          # print("Drawing bottom wall")
            start = Point(x1, y2)
            end = Point(x2, y2)
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

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_columns,
            cell_size_x,
            cell_size_y,
            win,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_columns = num_columns
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._cells = []
        self.win = win

        self._create_cells()

    def _create_cells(self):
        for i in range(self.num_rows):
            column = []
            
            for j in range(self.num_columns):
                cell = Cell(self.win)
                column.append(cell)
            self._cells.append(column)
        for i in range(self.num_rows):
            for j in range(self.num_columns):
                self._draw_cell(i,j)
        
    def _draw_cell(self, i, j):
        x1 = self.x1 + (j * self.cell_size_x)
        y1 = self.y1 + (i * self.cell_size_y)
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y

        cell = self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)
        

        
    










