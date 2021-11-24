file = open("MovieIndex/list.txt", "r")
for i in file:
    print(file.readlines(2))

file.close()