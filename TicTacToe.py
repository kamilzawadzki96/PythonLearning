import os

board = [[1, 2, 3], [4, 5, 6], [7 ,8 ,9]]
xory = 0

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

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    printBoard()

    #input index
    try:
        pole = int(input("Numer pola: "))
        if pole > 9 or pole < 1:
            print("Podaj ponownie wartosc z zakresu podanego na tablicy!")
            continue
    except ValueError:
        print("Wprowadz liczbe!")

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