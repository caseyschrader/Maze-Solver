from graphics import Line, Point

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
        self.visited = False

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
        from_midpoint = Point((self._x1 + self._x2)/2, (self._y1 + self._y2)/2)
        to_midpoint = Point((to_cell._x1 + to_cell._x2)/2, (to_cell._y1 + to_cell._y2)/2)
        line = Line(from_midpoint, to_midpoint)
        if undo == False:
            self._win.draw_line(line, fill_color="red")
        else:
            self._win.draw_line(line, fill_color="gray")