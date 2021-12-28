name = input("Give me your name: ")
lastname = input("Give me your lastname: ")
result = []

def reverse(x):
    for i in x:
        result.append(x[len(x)-x.index(i)-1])

reverse(lastname)
reverse(name)


print(" ".join(result))