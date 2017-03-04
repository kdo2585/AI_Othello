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



def main():
    print('Welcome to Othello!')
    mainBoard = getNewBoard()   #array of arrays(matrix)
    appendToArchive(boardsArchive, mainBoard)
    
    displayScore(mainBoard)
    drawBoard(mainBoard)
    
    mainBoard = changeBoard(mainBoard)
    playerColor = askColor()
    
    #beginTimer(10)  #10 seconds to make a move
    #GAMEPLAY HERE
    
    displayScore(mainBoard)
    calculateScore(mainBoard)
    
        
if __name__ == "__main__":
    main()

