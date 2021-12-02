from random import randrange

while True:
    random = str(randrange(10)) + str(randrange(10)) + str(randrange(10)) + str(randrange(10))

    try:
        user = int(input("Input your 4-digit number (ctrl + c to exit): "))
    except ValueError:
        print("Only integers!!!")
        continue

    struser = str(user)

    if len(struser) > 4:
        print("Too much digits")
        continue

    result = []
    cows = 0
    bulls = 0

    try:
        for i in range(len(struser)):
            if random[i] == struser[i]:
                result.append("Cow")
                cows += 1
            else:
                result.append("Bull")
                bulls += 1
    except ValueError:
        continue

    print(result)
    print("User input:", user)
    print("Computer rand:", random)
    print("Cows:",cows)
    print("Bulls:",bulls)