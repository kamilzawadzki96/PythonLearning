x = int(input("Podaj liczbe: "))
divisors = []
y = range(2, x+1)

for elem in y:
    try:
        if x % elem == 0:
            divisors.append(elem)
        else:
            continue
    except ZeroDivisionError:
        print("Nie dziel przez zero cholero")

print("Podzielniki liczby: ", x, "to: ", divisors)