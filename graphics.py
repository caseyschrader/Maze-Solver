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
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None

        self._win = win

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        
        # left line
        left_start = Point(x1, y1)
        left_end = Point(x1, y2)
        left_line = Line(left_start, left_end)
        #right line
        right_start = Point(x2, y1)
        right_end = Point(x2, y2)
        right_line = Line(right_start, right_end)
        #top line
        top_start = Point(x1, y1)
        top_end = Point(x2, y1)
        top_line = Line(top_start, top_end)
        #bottom line
        bottom_start = Point(x1, y2)
        bottom_end = Point(x2, y2)
        bottom_line = Line(bottom_start, bottom_end)

        if self.has_left_wall:
            self._win.draw_line(left_line)
        else:
            self._win.draw_line(left_line, fill_color="white")

        if self.has_right_wall:
            self._win.draw_line(right_line)
        else:
            self._win.draw_line(right_line, fill_color="white")
        
        if self.has_top_wall:
            self._win.draw_line(top_line)
        else:
            self._win.draw_line(top_line, fill_color="white")
        
        if self.has_bottom_wall:
            self._win.draw_line(bottom_line)
        else:
            self._win.draw_line(bottom_line, fill_color="white")
        
        

        



            


    def draw_move(self, to_cell, undo=False):
        from_midpoint = Point((self.__x1 + self.__x2)/2, (self.__y1 +self.__y2)/2)
        to_midpoint = Point((to_cell.__x1 + to_cell.__x2)/2, (to_cell.__y1 + to_cell.__y2)/2)
        line = Line(from_midpoint, to_midpoint)
        if undo == False:
            self._win.draw_line(line, fill_color="red")
        else:
            self._win.draw_line(line, fill_color="gray")

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_columns,
            cell_size_x,
            cell_size_y,
            win=None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_columns = num_columns
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._cells = []
        self._win = win


        self._create_cells()

    def _create_cells(self):
        for i in range(self.num_columns):
            column = []
            
            for j in range(self.num_rows):
                cell = Cell(self._win)
                column.append(cell)
            self._cells.append(column)
        for i in range(self.num_columns):
            for j in range(self.num_rows):
                self._draw_cell(i,j)
        
    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self.x1 + (j * self.cell_size_x)
        y1 = self.y1 + (i * self.cell_size_y)
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y

        cell = self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)
        
    def _break_entrance_and_exit(self):
        entrance_cell = self._cells[0][0]
        exit_cell = self._cells[-1][-1]

        entrance_cell.has_top_wall = False
        exit_cell.has_bottom_wall = False





        
    










