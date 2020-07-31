board = [[0 for i in range(5)] for j in range(5)]

def print_board(board):
    for row in board:
        print(row)
    print()

def get_moves(board,row,col):
    moves = [[-1,-1] for i in range(8)]
    start = 0
    for i in [-2,2]:
        for j in [-1,1]:
            if 0 <= row + i < len(board):
                if 0 <= col + j < len(board):
                    if board[row+i][col+j] == 0:
                        moves[start] = [row+i,col+j]
                        start += 1
    for i in [-1,1]:
        for j in [-2,2]:
            if 0 <= row + i < len(board):
                if 0 <= col + j < len(board):
                    if board[row+i][col+j] == 0:
                        moves[start] = [row+i,col+j]
                        start += 1
    return moves

def go(board,row,col,i=1,path=[[1,1]]):
    if i == len(board)**2:
        print(path)
    if i < len(board)**2:
        moves = get_moves(board,row,col)
        for move in moves:
            if move != [-1,-1]:
                board[row][col] = 1
                go(board,move[0],move[1],i+1,path+[move])
                board[row][col] = 0

go(board,0,0)
