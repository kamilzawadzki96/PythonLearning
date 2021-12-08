########

#Link to exercise https://www.practicepython.org/exercise/2015/11/26/27-tic-tac-toe-draw.html

########

import os

board = [[1, 2, 3], [4, 5, 6], [7 ,8 ,9]]

xory = 0

#reset board
def resetBoard():
    list = [[1, 2, 3], [4, 5, 6], [7 ,8 ,9]]
    return list

#print tab
def printBoard():
    for i in range (0,3):
        print(3* " ---")
        for y in range (0,3):
            print("|", board[i][y], end =" ")
            if y == 2:
                [print("|")]
        if i == 2:
            print(3* " ---")

def printWinner(win):
    print("And the winner is:", win)

while True:
    #definition of winner
    for i in range (0,3):
        if board[i][0] == board[i][1] == board[i][2] or board[0][i] == board[1][i] == board[2][i]:
            os.system('cls' if os.name == 'nt' else 'clear')
            printWinner(board[i][0])
            board = resetBoard()
            xory = 0
            input("Press key to continue...")

    #diagonally check
    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        os.system('cls' if os.name == 'nt' else 'clear')
        printWinner(board[0][0])
        board = resetBoard()
        xory = 0
        input("Press key to continue...")   

    #print board
    os.system('cls' if os.name == 'nt' else 'clear')
    printBoard()

    #display which player turn it is
    if xory == 0:
        print("\nIt's X turn\n")
    else:
        print("\nIt's Y turn\n")

    #input index
    try:
        pole = int(input("Input field index (Ctrl + C to exit): "))
        if pole > 9 or pole < 1:
            print("Input number between 1 and 9!")
            continue
    except ValueError:
        print("Input only numbers!")
        input("Press key to continue...")
        continue

    #value change in index
    for i in range (0,3):
        for y in range (0,3):
            if board[i][y] == pole:
                if xory == 0:
                    board[i][y] = "X"
                    xory = 1
                elif xory == 1:
                    board[i][y] = "Y"
                    xory = 0