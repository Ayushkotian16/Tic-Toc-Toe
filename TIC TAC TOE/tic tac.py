global game
# game board
board=["-","-","-",
       "-","-","-",
       "-","-","-"]
#DESIGNING GAME BOARD
def gameboard():
    print("\t"+board[0]+"\t|\t"+board[1]+"\t|\t"+board[2]+"\t\n")
    print("----------------------------------------------")
    print("\t"+board[3]+"\t|\t"+board[4]+"\t|\t"+board[5]+"\t\n")
    print("----------------------------------------------")
    print("\t"+board[6]+"\t|\t"+board[7]+"\t|\t"+board[8]+"\t\n")

# T O  P R I N T   X   I N   B O A R D

def printX(no,symbol):
    ch=int(input(f" PLAYER {no} ITS YOUR TURN ENTER POSITION TO PRINT {symbol}\n"))
    if ch<1 or ch>10:
        print("invalid")
        exit(0)
    if board[ch-1]=='-':
            board[ch-1]=symbol
    elif board[ch-1]!='-':
            print(f" PLAYER {no} THIS POSITION ALREADY OCCUIPIED")
            ch=int(input(f"PLAYER {no} RENTER POSITION TO PRINT X\n"))
            if board[ch-1]=='-':
                board[ch-1]=symbol

# C H E C K I N G   F O R   W I N N E R
def winner():
    #checking for player 1s winning
    if board[0]==board[1]==board[2]=='X':
        return True
    if board[3]==board[4]==board[5]=='X':
        return True
    if board[6]==board[7]==board[8]=='X':
        return True
    if board[0]==board[4]==board[8]=='X':
        return True
    if board[2]==board[4]==board[6]=='X':
        return True
    if board[0]==board[3]==board[6]=='X':
        return True
    if board[1]==board[4]==board[7]=='X':
        return True
    if board[2]==board[5]==board[8]=='X':
        return True
    #checking for player 2s winning
    if board[0]==board[1]==board[2]=='O':
        return True
    if board[3]==board[4]==board[5]=='O':
        return True
    if board[6]==board[7]==board[8]=='O':
        return True
    if board[0]==board[4]==board[8]=='O':
        return True
    if board[2]==board[4]==board[6]=='O':
        return True
    if board[0]==board[3]==board[6]=='O':
        return True
    if board[1]==board[4]==board[7]=='O':
        return True
    if board[2]==board[5]==board[8]=='O':
        return True

    else:
        return False
    
#checking for draw
def draw():
    if '-' not in board:
        return True
    else:
        return False
    

#game function
def startgame():
    print("Welcome to Tic Tac Toe!")
    print("You are Player 1, and you will be 'X'")
    print("You will play against the computer, which will be  Player 2 , and will be  'O'")
    print("To make a move, simply type the number of the space where you want to place")
    no=1
    symbol='X'
    game=True
    while game:
        gameboard()
        printX(no,symbol)
        if winner()==True:
            gameboard()
            print(f"PLAYER {no}WON!!!!")
            game=False
        elif draw()==True:
            gameboard()
            print("ITS DRAW")
            game=False
        if no==1:
            no=2
            symbol='O'
        else:
            no=1
            symbol='X'
#main loop
startgame()