lista = []

for i in range(1,51):
    lista.append(i)

res = list(filter(lambda x: x%2 == 0, lista))

print(res)