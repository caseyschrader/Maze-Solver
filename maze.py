from cell import Cell
import time
import random

"""
I think I have my i's and j's flipped, I went and flipped out create_cells was working and forgot to flip the logic for all other i and js. Making this note so I will fix someday
"""

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
            seed=None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_columns = num_columns
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._cells = []
        self._win = win
        self.seed = seed

        if seed:
            random.seed(seed)


        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls(0, 0)
        self._reset_cells_visited()

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
        time.sleep(0.04)
        
    def _break_entrance_and_exit(self):
        entrance_cell = self._cells[0][0]
        exit_cell = self._cells[-1][-1]

        entrance_cell.has_top_wall = False
        self._draw_cell(0, 0)
        exit_cell.has_bottom_wall = False
        self._draw_cell(self.num_rows - 1, self.num_columns - 1)

    def _break_walls(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True

        while True:
            to_visit = []

            if j > 0:
                left_neighbor = self._cells[i][j-1]
            else:
                left_neighbor = None
            
            if j + 1 < len(self._cells[0]):
                right_neighbor = self._cells[i][j+1]
            else:
                right_neighbor = None

            if i > 0:
                top_neighbor = self._cells[i-1][j]
            else:
                top_neighbor = None
            
            if i + 1 < len(self._cells):
                bottom_neighbor = self._cells[i+1][j]
            else:
                bottom_neighbor = None

            if left_neighbor is not None and not left_neighbor.visited:
                to_visit.append(left_neighbor)
            if right_neighbor is not None and not right_neighbor.visited:
                to_visit.append(right_neighbor)
            if top_neighbor is not None and not top_neighbor.visited:
                to_visit.append(top_neighbor)
            if bottom_neighbor is not None and not bottom_neighbor.visited:
                to_visit.append(bottom_neighbor)
            
            if len(to_visit) == 0:
                self._draw_cell(i,j)
                return
            
            chosen_neighbor = random.choice(to_visit)

            if chosen_neighbor == left_neighbor:
                current_cell.has_left_wall = False
                chosen_neighbor.has_right_wall = False
                new_i, new_j = i, j - 1
            
            elif chosen_neighbor == right_neighbor:
                current_cell.has_right_wall = False
                chosen_neighbor.has_left_wall = False
                new_i, new_j = i, j + 1
            
            elif chosen_neighbor == top_neighbor:
                current_cell.has_top_wall = False
                chosen_neighbor.has_bottom_wall = False
                new_i, new_j = i-1, j
            
            elif chosen_neighbor == bottom_neighbor:
                current_cell.has_bottom_wall = False
                chosen_neighbor.has_top_wall = False
                new_i, new_j = i + 1, j
            
            self._break_walls(new_i, new_j)


    def _reset_cells_visited(self):
        for column in self._cells:
            for cell in column:
                cell.visited = False
    

    def _solve_r(self, i, j):

        self._animate()
        current_cell = self._cells[i][j]
        current_cell.visited = True

        if current_cell is self._cells[-1][-1]: # if current cell is the exit
            return True
        

        if j > 0 and not current_cell.has_left_wall and not self._cells[i][j-1].visited:
            current_cell.draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                current_cell.draw_move(self._cells[i][j - 1], True)

        if j + 1 < len(self._cells[0]) and not current_cell.has_right_wall and not self._cells[i][j + 1].visited:
            current_cell.draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                current_cell.draw_move(self._cells[i][j + 1], True)
        
        if i > 0 and not current_cell.has_top_wall and not self._cells[i-1][j].visited:
            current_cell.draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                current_cell.draw_move(self._cells[i - 1][j], True)
        
        if i + 1 < len(self._cells) and not current_cell.has_bottom_wall and not self._cells[i + 1][j].visited:
            current_cell.draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                current_cell.draw_move(self._cells[i + 1][j], True)
        

        return False
    
    def solve(self):
        return self._solve_r(0, 0)





