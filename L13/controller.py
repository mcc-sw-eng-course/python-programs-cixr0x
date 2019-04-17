from piece import CheckerPiece 
from board import Board 
import time

class CheckersController:
    pieces = []
    def placePiece(self, piece, x, y):
        piece["alive"] = True        
        self.board.set_piece(x, y, piece)

    def buildPiece(self):
        return {
            "alive": None,
            "owner":None, 
            "type":"peon",
            "index":None            
        }

    def __init__(self):
        self.board = Board()
        self.current_player = 1
        for a in range(12):
            piece = self.buildPiece()
            piece["owner"] = 1
            piece["index"] = len(self.pieces)
            self.pieces.append(piece)
        
        for a in range(12):
            piece = self.buildPiece()
            piece["owner"] = 2
            piece["index"] = len(self.pieces)
            self.pieces.append(piece)

        self.placePiece(self.pieces[0], 1, 0)
        self.placePiece(self.pieces[1], 3, 0)
        self.placePiece(self.pieces[2], 5, 0)
        self.placePiece(self.pieces[3], 7, 0)
        self.placePiece(self.pieces[4], 0, 1)
        self.placePiece(self.pieces[5], 2, 1)
        self.placePiece(self.pieces[6], 4, 1)
        self.placePiece(self.pieces[7], 6, 1)
        self.placePiece(self.pieces[8], 1, 2)
        self.placePiece(self.pieces[9], 3, 2)
        self.placePiece(self.pieces[10], 5, 2)
        self.placePiece(self.pieces[11], 7, 2)

        self.placePiece(self.pieces[12], 0, 7)
        self.placePiece(self.pieces[13], 2, 7)
        self.placePiece(self.pieces[14], 4, 7)
        self.placePiece(self.pieces[15], 6, 7)
        self.placePiece(self.pieces[16], 1, 6)
        self.placePiece(self.pieces[17], 3, 6)
        self.placePiece(self.pieces[18], 5, 6)
        self.placePiece(self.pieces[19], 7, 6)
        self.placePiece(self.pieces[20], 0, 5)
        self.placePiece(self.pieces[21], 2, 5)
        self.placePiece(self.pieces[22], 4, 5)
        self.placePiece(self.pieces[23], 6, 5)

    #just a function to visualize the board
    def printSimple(self):
        board_string = ""
        for i in range(self.board.size_x):
            for j in range(self.board.size_y):
                content = " "
                piece = self.board.get_piece(j, i)

                if piece and piece["alive"]:
                    content = piece["owner"]
                board_string=board_string + "["+str(content)+"]"
            
            board_string=board_string + "\n"
        print (board_string)

    def move_is_valid(self, source_x, source_y, dest_x, dest_y):

        if (not self.check_piece_exist(source_x, source_y, dest_x, dest_y)):
            return False

        if (not self.check_inbounds(source_x, source_y, dest_x, dest_y)):
            return False

        if (not self.check_square_not_busy(source_x, source_y, dest_x, dest_y)):
            return False

        if (not self.check_can_move(source_x, source_y, dest_x, dest_y) ):
            return False
  
        return True

    def jump_is_valid(self, source_x, source_y, dest_x, dest_y):
        if (not self.check_piece_exist(source_x, source_y, dest_x, dest_y)):
            return False

        if (not self.check_inbounds(source_x, source_y, dest_x, dest_y)):
            return False

        if (not self.check_square_not_busy(source_x, source_y, dest_x, dest_y)):
            return False


        if (not self.check_can_jump(source_x, source_y, dest_x, dest_y)):
            return False
        return True

    def check_piece_exist(self, source_x, source_y, dest_x, dest_y):
        #print ("Check piece exist")
        source_piece = self.board.get_piece(source_x, source_y)
        if (not source_piece):
            #print ("Invalid move, there isnt even a piece in the source square")
            return False
        return True 

    def check_inbounds(self, source_x, source_y, dest_x, dest_y):
        #print ("Check inbounds")
        #check in bounds
        if ((dest_x < 0 or dest_y < 0 or dest_x >= self.board.size_x or dest_y >= self.board.size_y) ):
            #print ("Invalid move, piece will fall out of bounds")
            return False
        return True 

    def check_square_not_busy(self, source_x, source_y, dest_x, dest_y):
        #print ("Check not busy")
        #check quare not already busy
        dest_piece = self.board.get_piece(dest_x, dest_y)
        if (dest_piece != None):
            #print("Invalid move, destination square is alredy occupied")
            return False
        return True

    def check_can_move(self, source_x, source_y, dest_x, dest_y):
        #print ("Check can move")

        source_piece = self.board.get_piece(source_x, source_y)
        #check if can move
        if (source_piece["owner"] == 1):
            if (dest_y == source_y + 1 and (dest_x == source_x -1 or dest_x == source_x +1 ) ):
                return True

        if (source_piece["owner"] == 2):
            if (dest_y == source_y - 1 and (dest_x == source_x -1 or dest_x == source_x +1 ) ):
                return True

        if (source_piece["type"] == "king"):
            if ((dest_y == source_y + 1 and (dest_x == source_x -1 or dest_x == source_x +1 ) )
            or   (dest_y == source_y - 1 and (dest_x == source_x -1 or dest_x == source_x +1 ) )):
                return True

        #print("Invalid move")
        return False
    
    def check_can_jump(self, source_x, source_y, dest_x, dest_y):
        #print ("Check can jump")
        source_piece = self.board.get_piece(source_x, source_y)
        #check if can jump

        #TODO: Clean duplicated code
        if (source_piece["owner"] == 1 or source_piece["type"]=="king"):
            if (dest_y == source_y + 2 and dest_x == source_x -2  ):
                jumped_piece = self.board.get_piece(source_x -1 , source_y +1)
                if (not jumped_piece):
                    #print ("Invalid jump, there is no piece to jump")
                    return False
                if (jumped_piece["owner"]!= source_piece["owner"]):
                    return True

            if (dest_y == source_y + 2 and dest_x == source_x +2  ):
                jumped_piece = self.board.get_piece(source_x +1, source_y +1)
                if (not jumped_piece):
                    #print ("Invalid jump, there is no piece to jump")
                    return False
                if (jumped_piece["owner"]!= source_piece["owner"]):
                    return True
                

        if (source_piece["owner"] == 2 or source_piece["type"]=="king"):
            if (dest_y == source_y - 2 and dest_x == source_x -2  ):
                jumped_piece = self.board.get_piece(source_x -1 , source_y -1)
                if (not jumped_piece):
                    #print ("Invalid jump, there is no piece to jump")
                    return False
                if (jumped_piece["owner"]!= source_piece["owner"]):
                    return True

            if (dest_y == source_y - 2 and dest_x == source_x +2  ):
                jumped_piece = self.board.get_piece(source_x +1 , source_y -1)
                if (not jumped_piece):
                    #print ("Invalid jump, there is no piece to jump")
                    return False
                if (jumped_piece["owner"]!= source_piece["owner"]):
                    return True

        #print("Invalid jump")
        return False
            
    def move_piece(self, source_x, source_y, dest_x, dest_y):
        if (self.move_is_valid(source_x, source_y, dest_x, dest_y)):            
            self.board.set_piece(dest_x, dest_y, self.board.get_piece(source_x, source_y)) 
            self.board.set_piece(source_x, source_y, None)
            if (self.board.get_piece(dest_x, dest_y)["owner"] == 1 and dest_y == 7):
                self.board.get_piece(dest_x, dest_y)["type"] = "king"
            if (self.board.get_piece(dest_x, dest_y)["owner"] == 2 and dest_y == 0):
                self.board.get_piece(dest_x, dest_y)["type"] = "king"

            self.current_player = 2 if self.current_player == 1 else 1

        if (self.jump_is_valid(source_x, source_y, dest_x, dest_y)):
            self.board.set_piece(dest_x, dest_y, self.board.get_piece(source_x, source_y)) 
            self.board.set_piece(int((dest_x+source_x)/2), int((dest_y+source_y)/2), None)
            self.board.set_piece(source_x, source_y, None) 
            if (self.board.get_piece(dest_x, dest_y)["owner"] == 1 and dest_y == 7):
                self.board.get_piece(dest_x, dest_y)["type"] = "king"
            if (self.board.get_piece(dest_x, dest_y)["owner"] == 2 and dest_y == 0):
                self.board.get_piece(dest_x, dest_y)["type"] = "king"
            
            self.current_player = 2 if self.current_player == 1 else 1

    def available_moves(self, source_x, source_y):
        available_moves_list = []
        available_moves_list = available_moves_list + self.get_available_moves(source_x, source_y)

        return available_moves_list
    

    def available_jumps(self, source_x, source_y):
        available_jumps_list = []
        available_jumps_list = available_jumps_list + self.get_available_jumps(source_x, source_y)

        return available_jumps_list


    #gets available moves (not jumps) for a given square (if a piece is there)
    #returns a list of tuples
    def get_available_moves(self, x, y):
        piece = self.board.get_piece(x, y)
        possible_destinations = []
        available_moves = []
        if (not piece):
            return []
        
        possible_destinations.append( (x+1, y+1) )
        possible_destinations.append( (x-1, y+1) )
        possible_destinations.append( (x+1, y-1) )
        possible_destinations.append( (x-1, y-1) )

        for dest in possible_destinations:
        #    print ("Checking move is valid", x, y, dest[0], dest[1])
            if (self.move_is_valid(x, y, dest[0], dest[1])):
                available_moves.append(  (x, y, dest[0], dest[1])  )

        return available_moves

    #gets available moves (not jumps) for a given square (if a piece is there)
    #returns a list of tuples
    def get_available_jumps(self, x, y):
        piece = self.board.get_piece(x, y)

        possible_destinations = []
        available_jumps = []
        if (not piece):
            return []
        
        possible_destinations.append( (x+2, y+2) )
        possible_destinations.append( (x-2, y+2) )
        possible_destinations.append( (x+2, y-2) )
        possible_destinations.append( (x-2, y-2) )

        for dest in possible_destinations:
            if (self.jump_is_valid(x, y, dest[0], dest[1])):
                available_jumps.append( (x, y, dest[0], dest[1]) )

        return available_jumps


