import board
class TictacBoard(board.Board):
    def __init__(self):
        super().__init__(3, 3, ' ')
        
    
    def full_row_equals(self,row,state):
        for x in range(0, self.size_x):
            if (self.get_state(x, row)!=state):
                return False
        return True

    def full_column_equals(self,column,state):
        for y in range(0, self.size_y):
            if (self.get_state(column, y)!=state):
                return False
        return True

    def diagonal_equals(self, state):
        for i in range(0, self.size_x):
            if (self.get_state(i, i)!=state):
                return False
        return True

    def antidiagonal_equals(self, state):
        for i in range(0, self.size_x):
            print("x{} y{} state{}".format(i, self.size_x-1 - i, self.get_state(i, self.size_x-1 - i)))
            if (self.get_state(i, self.size_x-1 - i)!=state):
                return False
        return True

    def check_win(self, state):
        for i in range(0, self.size_x):
            if (self.full_column_equals(i, state)):
                return True
        
        for i in range(0, self.size_y):
            if (self.full_row_equals(i, state)):
                return True
        
        if (self.diagonal_equals(state)):
            return True
        
        if (self.antidiagonal_equals(state)):
            return True

        return False

    def check_tie(self):
        for i in range(0, self.size_x):
            for j in range(0, self.size_y):
                if (self.get_state(i, j) == " "):
                    return False
        return True