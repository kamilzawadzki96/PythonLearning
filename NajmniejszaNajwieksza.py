list = []

while True:
    x = input("Podaj liczbe (x i Enter aby zakonczyc dodawanie): ")
    if x == "x":
        break
    else:
        list.append(int(x))



lower = 0
higher = 0

for i in list:
    if i < lower:
        lower = i
    elif i > higher:
        higher = i

print("Najnizsza liczba z ciagu podanego to:", lower)
print("Najwyzsza liczga z caigu podanego to:", higher)

#drukowanie listy
print(list)