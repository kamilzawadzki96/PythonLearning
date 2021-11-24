import time

while True:
    x = input("Podaj liczbe elementow ciagu Fibonacciego: ")

    try:
        x = int(x)
    except ValueError:
        print("Wartosc nie jest liczba!")
        continue

    fibo = []
    start = time.time()
    for i in range(int(x)):
        if i == 0:
            fibo.append(i)
        elif i == 1:
            fibo.append(i)
        else:
            fibo.append(fibo[i-2]+fibo[i-1])
    
    print(fibo, "\n")

    print("--- %s seconds ---" % (time.time() - start))