from random import randrange

while True:
    random = str(randrange(10)) + str(randrange(10)) + str(randrange(10)) + str(randrange(10))

    user = input("Input your number: ")

    if len(user) > 4:
        print("Too much digits")
        continue

    result = []
    cows = 0
    bulls = 0

    try:
        for i in range(len(user)):
            if random[i] == user[i]:
                result.append("Cow")
                cows += 1
            else:
                result.append("Bull")
                bulls += 1
    except ValueError:
        continue

    print(result)
    print("Cows:",cows)
    print("Bulls:",bulls)