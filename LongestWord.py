txt = input()
#your code goes here
txt = txt.split(" ")

for i in range(len(txt)):
    if i == 0:
        result = txt[i]
    elif int(len(txt[i])) > len(result):
        result = txt[i]

print(result)