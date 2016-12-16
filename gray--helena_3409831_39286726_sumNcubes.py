#sumNcubes.py

def main():
    import math
    posInt = eval(input("Please input a number."))
    sum = 0
    for i in range(1, posInt+1):
            sum = sum +((i+1)**3)
            
    print("The sum of the cubes up to the number you chose is " + str(sum) + ".")
main()

## your choice of rabge combined withth (i+1) skips the 1**3 term in every sum
## also, specification calls for one argument, not an "input"

##  23/25

        
    
