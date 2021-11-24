string = input()

words = 1
letters = 0
aletter = 0

for char in string:
    if char == " ":
        words += 1
    elif char == "a" or char == "A":
        aletter += 1
    letters += 1

print("Words:",words,"\nLetters:",letters,"\nLiter A:",aletter)