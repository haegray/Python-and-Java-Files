#triArea.py
#This program calculates the area of a triangle.

import math

def main():
    print("This program calculates the area of a triangle using the length of it's three sides.")
    print("What are the lengths of the sides? Separate using commas and do not include units.")

    a, b, c = eval(input("a, b, c: "))
    s = (a + b + c)/2
    A = (s * (s - a) * (s - b) * ( s - c))
    B = math.sqrt(A)

    if A<0:
        print ("Area of triangle equates to a nonreal number.")

    else:
        B = math.sqrt(A)

        print()
        print("The area of the triangle is:", B)

main()
