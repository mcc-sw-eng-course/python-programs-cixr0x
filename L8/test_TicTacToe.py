import unittest
import tictac
import board


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
        
        
        
        