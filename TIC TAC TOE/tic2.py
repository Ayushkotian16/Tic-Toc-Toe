print("WELCOME LETS PLAY TIC TAC TOE")
global game

# game board00
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
gameboard()

# T O  P R I N T   X   I N   B O A R D


def printX():
    ch=int(input(" PLAYER 1 ITS YOUR TURN ENTER POSITION TO PRINT X\n"))
    if board[ch-1]=='-':
            board[ch-1]='X'
    elif board[ch-1]!='-':
            print(" PLAYER 1 THIS POSITION ALREADY OCCUIPIED")
            ch=int(input("PLAYER 1 RENTER POSITION TO PRINT X \n"))
            if board[ch-1]=='-':
                    board[ch-1]='X'
    gameboard()


# T O  P R I N T   O   I N   B O A R D


def printO():
    
    ch=int(input("PLAYER 2 ITS YOUR TURN ENTER POSITION TO PRINT O\n"))
    if board[ch-1]=='-':
            board[ch-1]='O'
    elif board[ch-1]!='-':
            print(" PLAYER 2 THIS POSITION ALREADY OCCUIPIED")
            ch=int(input("PLAYER 2 RENTER POSITION TO PRINT O\n"))
            if board[ch-1]=='-':
                    board[ch-1]='O'
    gameboard()

game=True


# C H E C K I N G   F O R   W I N N E R
def winner():
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

def draw():
    if '-' not in board    :
        return True
    else:
        return False
    

# M A I N   L O O P   O F   G A M E
while game:
        printX()
        winner()

        if winner()==True:
            print("PLAYER 1 WON!!!")
            game=False
        elif draw()==True:
            print("IT'S A DRAW!!!")
            game=False
        printO()
        winner()
        if winner()==True:
            print("PLAYER 2 WON!!!")
            game=False
        elif draw()==True:
            print("IT'S A DRAW!!!")
            game=False
        





