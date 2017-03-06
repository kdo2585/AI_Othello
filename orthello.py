# orthello

import random
import sys
import time


boardsArchive = []  #array of boards, holding all of them in a round


def drawBoard(board):
# This function prints out the board that it was passed. Returns None.
    HLINE = '  +---+---+---+---+---+---+---+---+'
    VLINE = '  |   |   |   |   |   |   |   |   |'

    print('    A   B   C   D   E   F   G   H')
    print(HLINE)
    for y in range(8):
        print(VLINE)
        print(y+1, end=' ')
        for x in range(8):
            print('| %s' % (board[x][y]), end=' ')
        print('|')
        print(VLINE)
        print(HLINE)

def getNewBoard():
    # Creates a brand new, blank board data structure.
    board = []
    for i in range(8):
        board.append([' '] * 8)
        
    # Starting pieces:
    board[3][3] = 'W'
    board[3][4] = 'B'
    board[4][3] = 'B'
    board[4][4] = 'W'
    return board


def displayScore(board):
    black = 0
    white = 0
    for list in board:
        for item in list:
            if(item == "W"):
                white+=1
            if(item == "B"):
                black+=1
    print("white: ", white)
    print("black: ", black)
    
    
def askColor():
    color = ""
    while(color != 'b' and color != 'w'):
        color = input("What color do you want to be? (b or w)")
    return color


def changeBoard(board):
    ans = ""
    while(ans != 'y' and ans != 'n'):
        ans = input("Do you want to change the board layout to 'BW/WB'?: (y or n)")
    if(ans == 'y'):
        board[3][3] = 'B'
        board[3][4] = 'W'
        board[4][3] = 'W'
        board[4][4] = 'B'
        drawBoard(board)
        appendToArchive(boardsArchive, board)
        return board
    else:
        return board


def beginTimer(t):
    while t:
        print(t, end='..n\r')
        time.sleep(1)
        t -= 1
    print('You did not make a move in 10 seconds, you lose. \n\n\n')


def appendToArchive(boardsArchive, mainBoard):
    boardsArchive.append(mainBoard)
    return boardsArchive


def calculateScore(board):
    black = 0
    white = 0
    for list in board:
        for item in list:
            if(item == "W"):
                white+=1
            if(item == "B"):
                black+=1
    if(black > white):
        print("Black wins")
    elif(white > black):
        print("White wins")
    else:
        print("Tie Game")

def aiMove(board, aiColor):
    playerConfirm('AI is about to move.')
    # Make a move (currently just takes first open spot)
    move_made = False
    for i in range(0, 8):
        for j in range(0, 8):
            if board[i][j] == ' ':
                board[i][j] = aiColor
                print('AI moves to ' + chr(65 + i) + str(j + 1))
                move_made = True
                break
        if move_made == True:
            break

    # No move can be made
    if move_made == False:
        print('AI cannot make a move.')

    appendToArchive(boardsArchive, board)
    return board

def playerMove(board, playerColor):
    move = input('Player, please make a move.')
    col = ord(move[:1]) - 65
    row = int(move[1:]) - 1
    while(board[col][row] != ' '):
        move = input('Not valid. Please make another move.')
        col = ord(move[:1]) - 65
        row = int(move[1:]) - 1
    board[col][row] = playerColor
    print('Player moves to ' + str(move))
    appendToArchive(boardsArchive, board)
    return board

def playerConfirm(message):
     ans = input(str(message) + ' Enter \'y\' to confirm, \'quit\' to end the game.')
     while ans != 'y':
         if ans == 'quit':
             sys.exit()
         ans = input(str(message) + ' Enter \'y\' to confirm, \'quit\' to end the game.')

def moveExists(board):
    for i in range(0, 8):
        for j in range(0,8):
            if board[i][j] == ' ':
                return True
    
def main():
    print('Welcome to Othello!')
    mainBoard = getNewBoard()   #array of arrays(matrix)
    appendToArchive(boardsArchive, mainBoard)
    
    displayScore(mainBoard)
    drawBoard(mainBoard)
    
    mainBoard = changeBoard(mainBoard)
    playerColor = askColor().upper()
    
    #beginTimer(10)  #10 seconds to make a move
    #GAMEPLAY HERE
    playerTurn = True
    if(playerColor == 'W'):
        playerTurn = False
    while(moveExists(mainBoard) == True):
        if(playerTurn == False):
            mainBoard = aiMove(mainBoard, 'B')
        else:
            mainBoard = playerMove(mainBoard, playerColor)
        
        displayScore(mainBoard)
        # need to display highlighted board here
        drawBoard(mainBoard)

        if(playerTurn == False):
            playerConfirm('Confirm AI move?')
        else:
            playerConfirm('Confirm Player move?')
        # then update flipped squares here
        displayScore(mainBoard)
        drawBoard(mainBoard)
        playerTurn = not playerTurn
            
    
    displayScore(mainBoard)
    calculateScore(mainBoard)
    
        
if __name__ == "__main__":
    main()

