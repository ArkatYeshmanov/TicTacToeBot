#TicTacToe
import random
import sys
#Creating a board
board = ['-','-','-',
         '-','-','-',
         '-','-','-']
#Setting a current player to X
currentPlayer='X'
winner = None
gameRunning = True
win = 0
#Printing a board
def printBoard(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])
#Recieving a player's input
def playerInput(board):
    try:
        inp = int(input('Pick a number from 1 to 9: '))
        if inp >= 1 and inp <= 9 and board[inp-1]== '-':
            board[inp-1] = currentPlayer
    except:
        print('You had to write an integer from 1 to 9. Also, the spot must be free.')
        gameRunning = False
#Checking horizontals
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != '-':
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[4] != '-':
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != '-':
        winner = board[6]
        return True
#Checking cloumns
def checkColumn(board):
    global winner
    if board[0] == board[3] == board[6] and board[6] != '-':
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[7] != '-':
        winner = board[7]
        return True
    elif board[2] == board[5] == board[8] and board[8] != '-':
        winner = board[8]
        return True
#Checking diagnols
def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != '-':
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[6] != '-':
        winner = board[2]
        return True
#Checking a tie
def checkTie(board):
    global gameRunning, win
    if '-' not in board and win == 0:
        
        gameRunning = False

        print('It is a tie')
    

#Creating a simple bot                            
def AImachine(board):
    global currentPlayer
    four = 4


    if currentPlayer == 'X':
        currentPlayer = 'O'
        if board[0] == 'O' and board[3] == 'O' and board[6] == '-':
            board[6] = 'O'
            currentPlayer = 'X'
        elif board[3] == 'O' and board[6] == 'O' and board[0] == '-':
            board[0] = 'O'
            currentPlayer = 'X'
        elif board[0] == 'O' and board[6] == 'O' and board[3] == '-':
            board[3] = 'O'
            currentPlayer = 'X'
        elif board[1] == 'O' and board[4] == 'O' and board[7] == '-':
            board[7] = 'O'
            currentPlayer = 'X'
        elif board[1] == 'O' and board[7] == 'O' and board[4] == '-':
            board[4] = 'O'
            currentPlayer = 'X'
        elif board[4] == 'O' and board[7] == 'O' and board[1] == '-':
            board[1] = 'O'
            currentPlayer = 'X'
        elif board[2] == 'O' and board[5] == 'O' and board[8] == '-':
            board[8] = 'O'
            currentPlayer = 'X'
        elif board[8] == 'O' and board[5] == 'O' and board[2] == '-':
            board[2] = 'O'
            currentPlayer = 'X'
        elif board[2] == 'O' and board[8] == 'O' and board[5] == '-':
            board[5] = 'O'
            
            currentPlayer = 'X'
        elif board[0] == 'O' and board[1] == 'O' and board[2] == '-':
            board[2] = 'O'
            currentPlayer = 'X'
        elif board[0] == 'O' and board[2] == 'O' and board[1] == '-':
            board[1] = 'O'
            currentPlayer = 'X'
        elif board[1] == 'O' and board[2] == 'O' and board[0] == '-':
            board[0] = 'O'
            currentPlayer = 'X'
        elif board[3] == 'O' and board[4] == 'O' and board[5] == '-':
            board[5] = 'O'
            currentPlayer = 'X'
        elif board[3] == 'O' and board[5] == 'O' and board[4] == '-':
            board[4] = 'O'
            currentPlayer = 'X'
        elif board[4] == 'O' and board[5] == 'O' and board[3] == '-':
            board[3] = 'O'
            currentPlayer = 'X'
        elif board[6] == 'O' and board[7] == 'O' and board[8] == '-':
            board[8] = 'O'
            currentPlayer = 'X'
        elif board[6] == 'O' and board[8] == 'O' and board[7] == '-':
            board[7] = 'O'
            currentPlayer = 'X'
        elif board[7] == 'O' and board[8] == 'O' and board[6] == '-':
            board[6] = 'O'
            currentPlayer = 'X'
        elif board[0] == 'O' and board[4] == 'O' and board[8] == '-':
            board[8] = 'O'
            currentPlayer = 'X'
        elif board[8] == 'O' and board[4] == 'O' and board[0] == '-':
            board[0] = 'O'
            currentPlayer = 'X'
        elif board[0] == 'O' and board[8] == 'O' and board[4] == '-':
            board[4] = 'O'
            currentPlayer = 'X'
        elif board[2] == 'O' and board[4] == 'O' and board[6] == '-':
            board[6] = 'O'
            currentPlayer = 'X'
        elif board[6] == 'O' and board[4] == 'O' and board[2] == '-':
            board[2] = 'O'
            currentPlayer = 'X'
        elif board[2] == 'O' and board[6] == 'O' and board[4] == '-':
            board[4] = 'O'
            currentPlayer = 'X'
        #Preventing the win of X
        elif board[0] == 'X' and board[3] == 'X' and board[6] == '-':
            board[6] = 'O'
            currentPlayer = 'X'
        elif board[3] == 'X' and board[6] == 'X' and board[0] == '-':
            board[0] = 'O'
            currentPlayer = 'X'
        elif board[0] == 'X' and board[6] == 'X' and board[3] == '-':
            board[3] = 'O'
            currentPlayer = 'X'
        elif board[1] == 'X' and board[4] == 'X' and board[7] == '-':
            board[7] = 'O'
            currentPlayer = 'X'
        elif board[1] == 'X' and board[7] == 'X' and board[4] == '-':
            board[4] = 'O'
            currentPlayer = 'X'
        elif board[4] == 'X' and board[7] == 'X' and board[1] == '-':
            board[1] = 'O'
            currentPlayer = 'X'
        elif board[2] == 'X' and board[5] == 'X' and board[8] == '-':
            board[8] = 'O'
            currentPlayer = 'X'
        elif board[8] == 'X' and board[5] == 'X' and board[2] == '-':
            board[2] = 'O'
            currentPlayer = 'X'
        elif board[2] == 'X' and board[8] == 'X' and board[5] == '-':
            board[5] = 'O'
            
            currentPlayer = 'X'
        elif board[0] == 'X' and board[1] == 'X' and board[2] == '-':
            board[2] = 'O'
            currentPlayer = 'X'
        elif board[0] == 'X' and board[2] == 'X' and board[1] == '-':
            board[1] = 'O'
            currentPlayer = 'X'
        elif board[1] == 'X' and board[2] == 'X' and board[0] == '-':
            board[0] = 'O'
            currentPlayer = 'X'
        elif board[3] == 'X' and board[4] == 'X' and board[5] == '-':
            board[5] = 'O'
            currentPlayer = 'X'
        elif board[3] == 'X' and board[5] == 'X' and board[4] == '-':
            board[4] = 'O'
            currentPlayer = 'X'
        elif board[4] == 'X' and board[5] == 'X' and board[3] == '-':
            board[3] = 'O'
            currentPlayer = 'X'
        elif board[6] == 'X' and board[7] == 'X' and board[8] == '-':
            board[8] = 'O'
            currentPlayer = 'X'
        elif board[6] == 'X' and board[8] == 'X' and board[7] == '-':
            board[7] = 'O'
            currentPlayer = 'X'
        elif board[7] == 'X' and board[8] == 'X' and board[6] == '-':
            board[6] = 'O'
            currentPlayer = 'X'
        elif board[0] == 'X' and board[4] == 'X' and board[8] == '-':
            board[8] = 'O'
            currentPlayer = 'X'
        elif board[8] == 'X' and board[4] == 'X' and board[0] == '-':
            board[0] = 'O'
            currentPlayer = 'X'
        elif board[0] == 'X' and board[8] == 'X' and board[4] == '-':
            board[4] = 'O'
            currentPlayer = 'X'
        elif board[2] == 'X' and board[4] == 'X' and board[6] == '-':
            board[6] = 'O'
            currentPlayer = 'X'
        elif board[6] == 'X' and board[4] == 'X' and board[2] == '-':
            board[2] = 'O'
            currentPlayer = 'X'
        elif board[2] == 'X' and board[6] == 'X' and board[4] == '-':
            board[4] = 'O'
            currentPlayer = 'X'
        
        elif board[4] == '-':
            board[4] = 'O'
            currentPlayer = 'X'
           
        elif board[2] == '-':
            board[2] = 'O'
            currentPlayer = 'X'
        elif board[6] == '-':
            board[6] = 'O'
            currentPlayer = 'X'
        elif board[8] == '-':
            board[8] = 'O'
            currentPlayer = 'X'
        elif board[1] == '-':
            board[1] = 'O'
            currentPlayer = 'X'
        elif board[3] == '-':
            board[3] = 'O'
            currentPlayer = 'X'
        elif board[7] == '-':
            board[7] = 'O'
            currentPlayer = 'X'
        elif board[5] == '-':
            board[5] = 'O'
            currentPlayer = 'X' 


#Checking a win        
def checkWin():
    global winner, gameRunning, win
    if  checkHorizontal(board) or checkColumn(board) or checkDiag(board):
        printBoard(board)
        print(f'The winner is {winner}')
    
        gameRunning = False
        win = 1
        
       
 #Running a code          
while gameRunning:
    printBoard(board)

    playerInput(board)
    checkWin()

    if not gameRunning:
        break

    checkTie(board)

    if not gameRunning:
        break

    AImachine(board)
    checkWin()
    checkTie(board)

