import math

def sense(a,b):
    pizza = b / a
    return pizza

while True:
    x = int(input("Podaj średnicę pizzy: "))
    y = int(input("Podaj cenę pizzy: "))

    azure = math.pi*((x/2)**2)

    print(str(int(azure)) + " cm^2 pizzy.")

    print(str(round(sense(azure, y),4)),"zl za 1 cm^2 pizzy")