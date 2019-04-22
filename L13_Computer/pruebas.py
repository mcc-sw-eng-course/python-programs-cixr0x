print("Hello")
square = [[None] * 8 for i in range(8)]
print(square)
print(type(square))
print(len(square))

board_matrix=[]
line_1=[0,1,0,1,0,1,0,1]
line_2=[1,0,1,0,1,0,1,0]
line_3=[0,1,0,1,0,1,0,1]
line_4=[0,0,0,0,0,0,0,0]
board_matrix.append(line_1)
board_matrix.append(line_2)
board_matrix.append(line_3)
board_matrix.append(line_4)
print(board_matrix)
print(board_matrix[0][1])
for i in range(len(board_matrix)):
    if(1 in board_matrix[i]):
        print("True")
    else:
        print("False")


