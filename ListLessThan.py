while True:
    y = []

    z = int(input("Podaj liczbe: "))

    for element in range(1,1001):
        if element <=z:
            y.append(element)

    print(y)