from tkinter  import *# note that module name has changed from Tkinter in Python 2 to tkinter in Python 3
from controller import CheckersController
import time
import os
class CheckersUI:

    

    def __init__(self, checkers_controller):
        self.checkers_controller = checkers_controller
        self.master = Tk()
        self.window_size_x = 512
        self.window_size_y = 512
        self.square_size_x = self.window_size_x / self.checkers_controller.board.size_x
        self.square_size_y = self.window_size_y / self.checkers_controller.board.size_y
        self.dark_color = "black"
        self.light_color = "white"
        self.selected_piece_color = "blue"
        self.available_move_color = "red"
        self.window = Canvas(self.master, width=self.window_size_x, height=self.window_size_y)
        self.window.bind("<Button-1>", self.handle_click)
        self.selected_piece = None
        self.dest = None
        self.available_moves = []

    def render(self):
        self.window.pack()

        #board_string = ""
        odd_square = True
        dark_peon_img = PhotoImage(file=os.getcwd()+"/dark_peon.png")
        light_peon_img = PhotoImage(file=os.getcwd()+"/light_peon.png")
        dark_king_img = PhotoImage(file=os.getcwd()+"/dark_king.png")
        light_king_img = PhotoImage(file=os.getcwd()+"/light_king.png")

        for i in range(self.checkers_controller.board.size_x):
            for j in range(self.checkers_controller.board.size_y):
                piece = self.checkers_controller.board.get_piece(i, j)

                
                fill_color = self.light_color if odd_square else self.dark_color
                if (self.selected_piece and self.selected_piece[0] == i and self.selected_piece[1]==j):
                    fill_color = self.selected_piece_color                    
                
                for available_move in self.available_moves:
                    if (available_move[2] == i and available_move[3]==j):
                        fill_color = self.available_move_color

                x = i*self.square_size_x
                y = j*self.square_size_y
                self.window.create_rectangle(
                    x, 
                    y, 
                    x+self.square_size_x, 
                    y+self.square_size_y, 
                    fill= fill_color
                )

                if piece:
                    owner = piece["owner"]
                    if (piece["type"] == "peon"):
                        self.window.create_image(x, y, anchor="nw", image=dark_peon_img if owner ==1 else light_peon_img)
                    elif (piece["type"] == "king"):
                        self.window.create_image(x, y, anchor="nw", image=dark_king_img if owner ==1 else light_king_img)
                    
                

                
                odd_square =  not odd_square
            odd_square =  not odd_square
                #board_string=board_string + "["+str(content)+"]"
            
            #board_string=board_string + "\n"
        
        mainloop()

    def handle_click(self, event):
        board_x = int(event.x / self.square_size_x)
        board_y = int(event.y / self.square_size_y)
        print ("clicked at square", board_x,board_y)
        piece = self.checkers_controller.board.get_piece(board_x, board_y)

        if (piece and (self.selected_piece != piece) and (piece["owner"] == self.checkers_controller.current_player)):
            self.selected_piece = (board_x, board_y)
            self.dest = None
        else:
            if (self.selected_piece):
                self.dest = (board_x, board_y)

        if (self.selected_piece):
            self.available_moves = self.checkers_controller.available_moves(self.selected_piece[0], self.selected_piece[1])
            self.available_moves = self.available_moves +  self.checkers_controller.available_jumps(self.selected_piece[0], self.selected_piece[1])

        if (self.selected_piece and self.dest):
            self.checkers_controller.move_piece(self.selected_piece[0], self.selected_piece[1], self.dest[0], self.dest[1])
            self.selected_piece = None
            self.available_moves = []

        print ("Selected piece: ", self.selected_piece, " Destination: ", self.dest)

        self.render()


    


   
c = CheckersController()
ui = CheckersUI(c)
print (c.pieces)
c.printSimple()
ui.render()
time.sleep(1)
c.move_piece(1, 0, 1, 1)
c.printSimple()
ui.render()
time.sleep(1)
c.move_piece(1, 0, 0, 1)
c.printSimple()
ui.render()
time.sleep(1)
c.move_piece(1, 2, 2, 3)
c.printSimple()
ui.render()
time.sleep(1)
c.move_piece(0, 5, 1, 4)
c.printSimple()
ui.render()
time.sleep(1)
c.move_piece(0, 5, 1, 4)
c.printSimple()
ui.render()
time.sleep(1)
print (c.available_moves())
print (c.available_jumps())
c.move_piece(2, 3, 0, 5)
c.printSimple()
print (c.available_moves())
print (c.available_jumps())

