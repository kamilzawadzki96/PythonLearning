from itertools import count, repeat

for i in count(1):
    print(i)
    print(list(map(str,repeat("Test", 4))))
    if i >= 5:
        break