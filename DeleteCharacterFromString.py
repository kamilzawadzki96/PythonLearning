x = "Czesc, jestem Kamil i lubie jesc zupe, np. wczoraj zjadlem ogorkowa, byla bardzo dobra"
x = "".join(i for i in x if i not in ",")
y = x.split(" ")

for i in y:
    print(i)