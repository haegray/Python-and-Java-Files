#largest.py

#This program is designed to print out the largest value of three input values.

def largest():
    print("Please input three numbers separated by commas to see the largest number of the three.")
    x, y, z = eval(input("numbers: "))

    if x >= y and x >= z:
        print(x)
    elif y >= x and y >= z:
        print(y)
        
    elif z >=x and z >= y:
        print(z)

largest()


#IOP:
#Please input three numbers separated by commas to see the largest number of the three.
#numbers: 1,2,3
#3
#>>> ================================ RESTART ================================
#>>> 
#Please input three numbers separated by commas to see the largest number of the three.
#numbers: 44,55,66
#66
#>>> ================================ RESTART ================================
#>>> 
#Please input three numbers separated by commas to see the largest number of the three.
#numbers: 541,654,1
