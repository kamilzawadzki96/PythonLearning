x = input("Input some integers, comma separated: ")

x = x.split(",")
x = map(int, x)

res = 0

for i in x:
    if i == 19:
        res += 1
    if res == 2:
        print(True)