import math

while True:
    try:
        r = float(input("Give me radius of circle:"))
    except ValueError:
        print("Give me integer only!")
        input("Press any key to continue...")
        continue

    area = math.pi * pow(r, 2)
    print(area)