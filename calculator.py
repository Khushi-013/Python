import math

def calculate_area():
    print("==================")
    print("Area Calculator 📐")
    print("==================")
    print("1) Triangle")
    print("2) Rectangle")
    print("3) Square")
    print("4) Circle")
    print("5) Quit")

    while True:
        shape = int(input("Which shape: "))

        if shape == 1:
            b = float(input("Base: "))
            h = float(input("Height: "))
            area = (b * h) / 2
            print(f"The area is {area}\n")
        elif shape == 2:
            l = float(input("Length: "))
            b = float(input("Breadth: "))
            area = l * b
            print(f"The area is {area}\n")
        elif shape == 3:
            s = float(input("Side: "))
            area = s ** 2
            print(f"The area is {area}")
        elif shape == 4:
            r = float(input("Radius: "))
            area = math.pi * (r ** 2)
            print(f"The area is {area}")
        elif shape == 5:
            print("Existing the calculator. Goodbye!")
            break
        else:
            print("Invalid choice")

calculate_area()

