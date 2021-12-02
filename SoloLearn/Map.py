def square(x):
    return x**2

lista = []

"""
while True:
    x = input("Input (x to exit input):")
    if x == "x":
        print("Bye")
        break
    
    lista.append(int(x))
"""

for i in range(1,51):
    lista.append(i)

print(lista)

print(list(map(square,lista)))