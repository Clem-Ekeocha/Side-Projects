'''
This is a program developed for calculating the area of a rectangle
'''

try:
    length = float(input("Kindly enter the length of the rectangle: "))
    width = float(input("Kindly enter the width of the rectangle: "))

    if length == width:
        exit("Both length and width are same and it's a square")

    area = length * width
    print(f" The area of the rectangle is {area}")
except ValueError:
    print("Please enter a number.")
