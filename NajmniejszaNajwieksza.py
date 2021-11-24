list = [10, -4, 20, 50, 60, 70 , 100, -50, -40]

lower = 0
higher = 0

for i in list:
    if i < lower:
        lower = i
    elif i > higher:
        higher = i

print(lower)
print(higher)
