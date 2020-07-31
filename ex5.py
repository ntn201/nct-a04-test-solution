maze = [["V","i","n","h"],
        ["i","n","h","-"],
        ["n","h","-","-"],
        ["h","-","-","-"]]


def get_moves(maze,row,col):
    moves = [[-1,-1] for i in range(4)]
    if row > 0 and maze[row-1][col] != "*":
        moves[0] = [row-1,col]        
    if row < len(maze)-1 and maze[row+1][col] != "*":
        moves[1] = [row+1,col]
    if col > 0 and maze[row][col-1] != "*":
        moves[2] = [row,col-1]
    if col < len(maze[row]) - 1 and maze[row][col+1] != "*":
        moves[3] = [row,col+1]
    return moves

def go(maze,row,col,path=[[0,0]],string=""):
    if string + maze[row][col] == "Vinh":
        print(path)
    else:
        moves = get_moves(maze,row,col)
        for move in moves:
            if move != [-1,-1]:
                temp = maze[row][col]
                maze[row][col] = "*"
                go(maze,move[0],move[1],path+[move],string+temp)
                maze[row][col] = temp

go(maze,0,0)