import unittest
import tictac
import board
import tictacBoard


class TestTictac(unittest.TestCase):
    
    def test_board(self):
        brd=board.Board(3,3,"")
        self.assertEqual(brd.board, [['', '', ''], ['', '', ''], ['', '', '']])
        brd.set_state(2,2,"X")
        self.assertEqual(brd.board,[['', '', ''], ['', '', ''], ['', '', 'X']])
        state=brd.get_state(2, 2)
        self.assertEqual(state,"X")
        #msg="|  |  | \n------------\n |  |  | \n------------\n |  | X | \n------------\n"
        #printedBoard=brd.draw()
        #self.assertEqual(printedBoard,msg)
    
    def test_tictacBoard(self):
        brd = tictacBoard.TictacBoard()
        self.assertFalse(brd.full_row_equals(0, "X"))
        brd.set_state(0, 0, "X")
        brd.set_state(1, 0, "X")
        brd.set_state(2, 0, "X")
        self.assertTrue(brd.full_row_equals(0, "X"))

        self.assertFalse(brd.full_column_equals(0, "X"))
        brd.set_state(0, 0, "X")
        brd.set_state(0, 1, "X")
        brd.set_state(0, 2, "X")
        self.assertTrue(brd.full_column_equals(0, "X"))

        self.assertFalse(brd.diagonal_equals("X"))
        self.assertFalse(brd.antidiagonal_equals("X"))
        brd.set_state(1, 1, "X")
        brd.set_state(2, 2, "X")
        self.assertTrue(brd.diagonal_equals("X"))
        self.assertTrue(brd.antidiagonal_equals("X"))

        self.assertEqual(brd.get_available_coords(), [[1, 2], [2, 1]] )

        brd_win = tictacBoard.TictacBoard()
        self.assertFalse(brd_win.check_win("X"))
        brd_win.set_state(0, 2, "X")
        brd_win.set_state(1, 1, "X")
        brd_win.set_state(2, 0, "X")
        self.assertTrue(brd_win.check_win("X"))
        brd_win.set_state(0, 0, "X")
        brd_win.set_state(1, 1, "X")
        brd_win.set_state(2, 2, "X")
        self.assertTrue(brd_win.check_win("X"))
        brd_win.set_state(1, 0, "X")
        self.assertTrue(brd_win.check_win("X"))
        brd_win.set_state(0, 1, "X")
        self.assertTrue(brd_win.check_win("X"))
        self.assertFalse(brd_win.check_tie())
        brd_win.set_state(2, 1, "0")
        brd_win.set_state(1, 2, "0")
        self.assertTrue(brd_win.check_tie())
        brd.draw_tictac()
        

if __name__ == '__main__':
    unittest.main()
        