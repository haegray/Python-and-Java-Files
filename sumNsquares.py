#sumNcubes.py

def main():
    import math
    posInt = eval(input("Please input a number."))
    sum = 0
    for i in range(1, posInt+1):
            sum = sum +((i+1)**2)
            
    print("The sum of the cubes up to the number you chose is " + str(sum) + ".")
main()


        
    
