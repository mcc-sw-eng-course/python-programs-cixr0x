'''
Created on 2018 M12 26

@author: A01221781
'''
from random import randint
board = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3']]
print(str(5)in board[1])


def draw(board):
    numRows = len(board)
    numColumns = len(board[0])
    for i in range(0, numRows):
        for j in range(0, numColumns):
            print(board[i][j], end=" | ")
        print()
        print("------------")


def available(location, board):
    numRows = len(board)
    numColumns = len(board[0])
    available = False
    for i in range(0, numRows):
        if(str(location) in board[i]):
            available = True
            break
    print(available)
    return available


def mark(player, location, board):
    numRows = len(board)
    numColumns = len(board[0])
    if(available(location, board)):
        for i in range(0, numRows):
            for j in range(0, numColumns):
                if(board[i][j] == str(location)):
                    board[i][j] = str(player)
    else:
        print("Space not available, try again")
    draw(board)


def check_win(board):
    win = False
    numRows = len(board)
    numColumns = len(board[0])
    # Horizontal win
    for i in range(0, numRows):
        if(board[i][0].lower() == "x"):
            for j in range(1, numColumns):
                if(board[i][j].lower() == "x"):
                    win = True
                else:
                    win = False
                    break
        elif(board[i][0].lower() == "o"):
            for j in range(1, numColumns):
                if(board[i][j].lower() == "o"):
                    win = True
                else:
                    win = False
                    break
        else:
            continue
    if(win == True):
        return win
    # Vertical win
    for i in range(0, numColumns):
        if(board[0][i].lower() == "x"):
            for j in range(1, numRows):
                if(board[j][i].lower() == "x"):
                    win = True
                else:
                    win = False
                    break
        elif(board[0][i].lower() == "o"):
            for j in range(1, numRows):
                if(board[j][i].lower() == "o"):
                    win = True
                else:
                    win = False
                    break
        else:
            continue
    if(win == True):
        return win

    # diagonal win
    i = 0
    if(board[i][i].lower() == "x"):
        for j in range(1, numRows):
            if(board[j][j].lower() == "x"):
                win = True
            else:
                win = False
                break
    elif(board[i][i].lower() == "o"):
        for j in range(1, numRows):
            if(board[j][j].lower() == "o"):
                win = True
            else:
                win = False
                break

    else:
        win = False
    if(win == True):
        return win
    # anti-diagonal win
    i = 2
    if(board[0][i].lower() == "x"):
        j = 1
        k = 1
        while(j >= 0):
            if(board[k][j].lower() == "x"):
                win = True
                j = j - 1
                k = k + 1
            else:
                win = False
                j = -1
    elif(board[0][i].lower() == "o"):
        j = 1
        k = 1
        while(j >= 0):
            if(board[k][j].lower() == "o"):
                win = True
                j = j - 1
                k = k + 1
            else:
                win = False
                j = -1

    else:
        win = False
    return win


def check_tie(board):
    tie = False
    numRows = len(board)
    numColumns = len(board[0])
    if(check_win(board) == False):
        for i in range(0, numRows):
            for j in range(0, numColumns):
                if(board[i][j].lower() == "x"or board[i][j].lower() == "o"):
                    tie = True
                else:
                    tie = False
                    break
    else:
        tie = False
    return tie


def dashes():
    # print a line of dashes
    print("o" + 35 * '-' + "o")


def display_message(message):
    print("|{:^35s}|".format(message))


def main():
    # initializing game
    board = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3']]
    # select the first player randomly
    player = ['X', 'O']
    turn = randint(0, 1)

    win = False
    tie = False
    while(not win and not tie):
        # switch players
        turn = (turn + 1) % 2
        current_player = player[turn]  # contains 'X' or 'O'

        # display header
        dashes()
        print("TIC TAC TOE")
        dashes()

        # display game board
        print()
        draw(board)
        print()

        # display footer
        dashes()
        # player select a location to mark
        while True:
            location = input(
                "|{:s} Turn, select a number (1, 9): ".format(current_player))
            if available(location, board):
                break  # Only the user input loop, main loop does NOT break
            else:
                print("Selection not available!")
        dashes()

        # mark selected location with player symbol ('X' or 'O')
        mark(current_player, location, board)

        # check for win
        win = check_win(board)

        # check for tie
        tie = check_tie(board)

    # Display game over message after a win or a tie
    # clear_output()

    # display header
    dashes()
    print("TIC TAC TOE")
    dashes()

    # display game board (Necessary to draw the latest selection)
    print()
    draw(board)
    print()

    # display footer
    dashes()
    print("Game Over!")
    if(tie):
        print("Tie!")
    elif(win):
        print("Winner:")
        print(current_player)
    dashes()


# Run the game
main()


# draw(board)
#available(5, board)
#mark("o", 5, board)
#mark("O", 7, board)
#print("Win?:", check_win(board))
#mark("O", 3, board)
#print("Win?:", check_win(board))
# dashes()
# display_message("Elisaf")
