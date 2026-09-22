# FEATURES
# Find AREA and PERIMETER of:
# --- Square
# --- Rectangle
# --- Circle
# --- Triangle
#
# Find VOLUME of:
# --- Cube
# --- Cuboid
# --- Cylinder
pie = 22 / 7

# Area

def square_area():
    side = float(input("Enter Side of Square: "))
    area = side * side
    print(f"The Area of Square is {area}")


def rectangle_area():
    length = float(input("Enter Length of Rectangle: "))
    breadth = float(input("Enter Breadth of Rectangle: "))
    area = length * breadth
    print(f"The Area of Rectangle is {area}")


def circle_area():
    radius = float(input("Enter Radius of Circle: "))
    area = pie * radius * radius
    print(f"The Area of Circle is {area}")


# Perimeter

def square_perimeter():
    side = float(input("Enter Side of Square: "))
    perimeter = 4 * side
    print(f"The Perimeter of Square is {perimeter}")


def rectangle_perimeter():
    length = float(input("Enter Length of Rectangle: "))
    breadth = float(input("Enter Breadth of Rectangle: "))
    perimeter = 2 * (length + breadth)
    print(f"The Perimeter of Rectangle is {perimeter}")


def circle_perimeter():
    radius = float(input("Enter Radius of Circle: "))
    perimeter = 2 * pie * radius
    print(f"The Perimeter of Circle is {perimeter}")


# Volume

def cube_volume():
    side = float(input("Enter Side of Cube: "))
    volume = side * side * side
    print(f"The Volume of Cube is {volume}")


def cuboid_volume():
    length = float(input("Enter Length of Cuboid: "))
    breadth = float(input("Enter Breadth of Cuboid: "))
    height = float(input("Enter Height of Cuboid: "))
    volume = length * breadth * height
    print(f"The Volume of Cuboid is {volume}")




while True:
    print("\n===== MATH TOOLS =====\n")
    print("1. Square Area")
    print("2. Rectangle Area")
    print("3. Circle Area")
    print("4. Square Perimeter")
    print("5. Rectangle Perimeter")
    print("6. Circle Perimeter")
    print("7. Cube Volume")
    print("8. Cuboid Volume")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        square_area()

    elif choice == "2":
        rectangle_area()

    elif choice == "3":
        circle_area()

    elif choice == "4":
        square_perimeter()

    elif choice == "5":
        rectangle_perimeter()

    elif choice == "6":
        circle_perimeter()

    elif choice == "7":
        cube_volume()

    elif choice == "8":
        cuboid_volume()

    elif choice == "9":
        print("Goodbye! 👋")
        break

    else:
        print("❌ Invalid choice!")
