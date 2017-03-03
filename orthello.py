# orthello

import random
import sys

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
    board[3][3] = 'B'
    board[3][4] = 'W'
    board[4][3] = 'W'
    board[4][4] = 'B'
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


def main():
    print('Welcome to Othello!')
    mainBoard = getNewBoard()   #array of arrays(matrix)
    
    displayScore(mainBoard)
    drawBoard(mainBoard)
    playerColor = askColor()
    
        
if __name__ == "__main__":
    main()

