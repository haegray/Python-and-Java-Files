#sumN.py

#This program is designed to print out the sum of numbers 1 to N.

def sumN():
    print("Please enter the amount of numbers increasing by one you would like to be summed.")
    N = eval(input("N: "))
    total = ((1 + N)*(N/2))
    print()
    print("The sum is", total)

sumN()


#IOP:            
#Please enter the amount of numbers increasing by one you would like to be summed.
#N: 15

#The sum is 120.0
#Please enter the amount of numbers increasing by one you would like to be summed.
#N: 10

#The sum is 55.0
