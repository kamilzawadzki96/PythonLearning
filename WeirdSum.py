while True:
    try:
        x = int(input("Input some integer: "))
    except ValueError:
        print("I said, ONLY INTEGERS!!!")
        input("Press enter to continue...")
        continue

    print(x + int(str(x)+str(x)) + int(str(x)+str(x)+str(x)))