def primal(a):
    for i in range(2,a-1):
        if a % i == 0 and i != a:
            return False
        else:
            return True

while True:
    x = input("Podaj liczbe (exit, aby zakonczyc): ")

    if x == "exit":
        break

    try:
        if primal(int(x)) == False:
            print("Liczba:", x, "nie jest liczba pierwsza.")
        else:
            print("Liczba:", x, "jest liczba pierwsza!")
    except ValueError:
        print("Wartosc podana nie jest liczba, podaj ponownie!")
        continue