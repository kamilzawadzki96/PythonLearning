import random
import time

user = 0
comp = 0

while True:
    #input
    choice = input("Wybierz orzel czy reszka (o / r), Enter aby zakonczyc: ")

    """
    if choice != "o" or choice != "r" or choice != "":
        print("Podales zla wartosc, sprobuj jeszcze raz. Wybrana wartosc: ", choice)
        continue
    elif choice == "":
        break
    """

    for i in range(3):
        print(3-i)
        time.sleep(0.75)
    
    x = random.choice(["orzel","reszka"])

    if x == "orzel" and choice == "o":
        print("Wygrales! Wynik to Orzel\n")
        user += 1
    elif x == "reszka" and choice == "r":
        print("Wygrales! Wynik to Reszka\n")
        user += 1
    else:
        print("Przegrales!\n")
        comp += 1
    
    print("Wynik uzytkownika:",user)
    print("Wynik komputera:",comp)