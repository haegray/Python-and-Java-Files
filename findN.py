#findN.py
#This is a program designed to find how many terms of a series must be added
#together to make the sum greater than the user input 'M'.
 
def findN():
    
    print("Please enter a number you would like the sum to be greater than to find out how many terms must be added to make it so.")
    M = eval(input("M: "))
    k=1
    finValue = 1/k
    
    while finValue <= M:
        k=k+1
        N=k
        finValue = finValue + (1/k)

    print("The number of terms to be added is", N)

findN()

#IOP:

#Please enter a number you would like the sum to be greater than to find out how many terms must be added to make it so.
#M: 10
#The number of terms to be added is 12367

#Please enter a number you would like the sum to be greater than to find out how many terms must be added to make it so.
#M: 11
#The number of terms to be added is 33617
