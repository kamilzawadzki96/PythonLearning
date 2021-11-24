import random

while True:
    x = input("Podaj liczbe z zakresu 1-9, exit aby opuscic gre: ")
    try:
        if x == "exit":
            print("Wylaczanie gry!")
            break
        elif int(x) < 1 or int(x) > 9:
            print("Podales zla wartosc, spoza zakresu")
            continue
    except ValueError:
        print("Nieprawidlowa wartosc!")
        continue
    
    choice = random.choice(range(1,10))
    if int(x) == choice:
        print("Wygrales, wybrane liczby - komputer: ", choice, "gracz:", x)
    else:
        print("Przegrales, wybrane liczby - komputer: ", choice, "gracz:", x)
