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