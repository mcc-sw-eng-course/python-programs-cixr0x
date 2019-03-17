
import tictac


tt = tictac.Tictac()
tt.board.set_state(2, 0, 'X')
tt.board.set_state(2, 1, 'X')
tt.board.set_state(2, 2, 'X')
tt.board.set_state(1, 0, 'X')
tt.board.set_state(1, 1, 'X')
tt.board.set_state(1, 2, 'X')
tt.board.set_state(0, 0, 'X')
tt.board.set_state(0, 1, 'X')
#tt.board.set_state(0, 2, 'X')
print(tt.board.full_row_equals(0, 'X'))
print(tt.board.full_column_equals(0, 'X'))
print(tt.board.diagonal_equals('X'))
print(tt.board.antidiagonal_equals('X'))
print(tt.board.check_win('X'))
print(tt.board.check_tie())
tt.board.draw()