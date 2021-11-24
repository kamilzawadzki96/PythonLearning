import random
import getpass

comp = 0
user = 0

games = int(input("Podaj ilosc rozgrywek: "))

for i in range(games):
    x = getpass.getpass("Gracz1 Kamien (k) / Papier (p) / Nozyce (n): ")
    y = getpass.getpass("Gracz2 Kamien (k) / Papier (p) / Nozyce (n): ")
    #choice = random.choice(["k","p","n"])
       

    if x == y:
        print("Remis!")
        continue
    elif x == "k":
        if y == "p":
            print("Wygral Gracz 2!")
            comp += 1
        else:
            print("Wygral Gracz 1!")
            user += 1
        continue
    elif x == "p":
        if y == "n":
            print("Wygral Gracz 2!")
            comp += 1
        else:
            print("Wygral Gracz 1")
            user += 1
        continue
    elif x == "n":
        if y == "k":
            print("Wygral Gracz 2!")
            comp += 1
        else:
            print("Wygral Gracz1!")
            user += 1
        continue

print("Wynik po ",games," rozgrywkach:")
print("Gracz 1: ", user)
print("Gracz 2: ", comp)
if comp > user:
    print("Wygral Gracz 2!")
else:
    if comp == user:
        print("Remis!")
    else:
        print("Wygral Gracz 1!")
