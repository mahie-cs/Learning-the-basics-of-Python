# I made a calculator that calculates area of six different shapes.
# I have done it before in C, but it wasn't persistent.
# So this time I used a loop that is true until it breaks.
# I also ran a debugger to check for bugs. This script should have no bugs.
# I first made this whole script with sys lib and was using sys.exit() to close this script on invalid input.
# Which obviously worked. But it felt like I was punishing the user for every typo.
# So ultimately I ended up with this as a solution.

import math

while True:
    print("\n--- Area Calculator ---")
    print("Choose a shape to calculate the area:")
    print("1. Square")
    print("2. Rectangle")
    print("3. Triangle")
    print("4. Circle")
    print("5. Parallelogram")
    print("6. Trapezoid")
    print("7. Exit Program")

    try:
        choice = int(input("Enter your choice (1-7): "))
    except ValueError:
        print("Invalid choice. Please enter a number.")
        continue

    if choice == 7:
        print("Goodbye!")
        break

    if choice < 1 or choice > 7:
        print("Invalid choice. Please choose a number between 1 and 7.")
        continue

    match choice:
        case 1:
            try:
                side = float(input("Enter the side length of the square: "))
            except ValueError:
                print("Invalid input. Must be a number.")
                continue
            if side <= 0:
                print("Invalid side length. Must be greater than 0.")
                continue
            area = side * side
            print(f"Square area: {area:.2f}")

        case 2:
            try:
                length = float(input("Enter the length of the rectangle: "))
            except ValueError:
                print("Invalid input.")
                continue
            if length <= 0:
                print("Invalid length.")
                continue
            try:
                width = float(input("Enter the width of the rectangle: "))
            except ValueError:
                print("Invalid input.")
                continue
            if width <= 0:
                print("Invalid width.")
                continue
            area = length * width
            print(f"Rectangle area: {area:.2f}")

        case 3:
            try:
                base = float(input("Enter the base of the triangle: "))
            except ValueError:
                print("Invalid input.")
                continue
            if base <= 0:
                print("Invalid base.")
                continue
            try:
                height = float(input("Enter the height of the triangle: "))
            except ValueError:
                print("Invalid input.")
                continue
            if height <= 0:
                print("Invalid height.")
                continue
            area = 0.5 * base * height
            print(f"Triangle area: {area:.2f}")

        case 4:
            try:
                radius = float(input("Enter the radius of the circle: "))
            except ValueError:
                print("Invalid input.")
                continue
            if radius <= 0:
                print("Invalid radius.")
                continue
            area = math.pi * radius * radius
            print(f"Circle area: {area:.2f}")

        case 5:
            try:
                base = float(input("Enter the base of the parallelogram: "))
            except ValueError:
                print("Invalid input.")
                continue
            if base <= 0:
                print("Invalid base.")
                continue
            try:
                height = float(input("Enter the height of the parallelogram: "))
            except ValueError:
                print("Invalid input.")
                continue
            if height <= 0:
                print("Invalid height.")
                continue
            area = base * height
            print(f"Parallelogram area: {area:.2f}")

        case 6:
            try:
                base1 = float(input("Enter the first base of the trapezoid: "))
            except ValueError:
                print("Invalid input.")
                continue
            if base1 <= 0:
                print("Invalid first base.")
                continue
            try:
                base2 = float(input("Enter the second base of the trapezoid: "))
            except ValueError:
                print("Invalid input.")
                continue
            if base2 <= 0:
                print("Invalid second base.")
                continue
            try:
                height = float(input("Enter the height of the trapezoid: "))
            except ValueError:
                print("Invalid input.")
                continue
            if height <= 0:
                print("Invalid height.")
                continue
            area = 0.5 * (base1 + base2) * height
            print(f"Trapezoid area: {area:.2f}")
