import os

files = [f for f in os.listdir('.') if os.path.isfile(f)]

for e in files:
    print("Extension of file", e.split(".")[len(e.split("."))-2], "is", e.split(".")[len(e.split("."))-1])