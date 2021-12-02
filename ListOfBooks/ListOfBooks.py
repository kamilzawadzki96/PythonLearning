#funkcje

#listowanie ksiazek
def list():
    try:
        textfile = open("list.txt", "x")
    except FileExistsError:
        print("Plik nie istnieje!")
    finally:
        textfile = open("list.txt")

    with textfile as f:
        list = f.read().splitlines()
    textfile.close()

    for book in list:
        print(str(list.index(book)+1) + ". " + book)

    wait = input("")

    textfile.close()

#dodawanie ksiazek
def addbook():
    while True:
        newbook = str(input("Podaj nazwę nowej ksiazki (Enter aby zakonczyc): "))
        if newbook == "":
            break
        else:
            textfile = open("list.txt", "a")
            try:
                textfile.write("\n" + newbook)
            except:
                print("Blad!")
                break
            textfile.close()

#switch case menu
def switch(x):
    match x:
        case "1":
            list()
        case "2":
            addbook()
        case "x":
            return 1

#glowna petla programu
while True:

    #case
    print("\n")
    print("1. Wylistuj ksiazki")
    print("2. Dodaj nowa ksiazke")
    print("x. Wylacz program")
    x = str(input("Podaj co chcesz zrobic: "))
    if switch(x) == 1:
        break