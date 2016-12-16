#slope.py
# A program used to calculate the slope of a line.

def main():
    print("This program will calculate the slope of a line.")
    print()
    print("Please enter the values for the x and y coordinates.")
    (X1,Y1) = eval(input("Input the first point separated by a comma."))
    (X2,Y2) = eval(input("Input the second point separated by a comma."))
    slopeY = Y2 - Y1
    slopeX = X2 - X1
    if slopeX == 0:
        print("The slope is undefined.")
    else:
        print("The slope is", slopeY,"/",slopeX)

main()
