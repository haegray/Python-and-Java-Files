# File: chaos.py
#A simple program illustrating chaotic behavior.

def main():
    print("This program illustrates a chaotic function")
    x= eval(input("Enter a number between 0 and 1: "))
    n = eval(input("How many numbers should I print? "))
    for i in range(n):
        x = 2.0 * x * (1-x)
        print(x)

main()


#In the original chaos program with a value of '3.9' the output values
#were varied within the range of 0 and 1. The outputs of the altered
#chaos program where the value was changed to '2.0' were much more close
#in value, most only varying by hundredths.

#This program illustrates a chaotic function
#Enter a number between 0 and 1: .7
#How many numbers should I print? 15
#0.42000000000000004
#0.4872
#0.49967231999999995
#0.4999997852516352
#0.4999999999999078
#0.49999999999999994
#0.49999999999999994
#0.49999999999999994
#0.49999999999999994
#0.49999999999999994
#0.49999999999999994
#0.49999999999999994
#0.49999999999999994
#0.49999999999999994
#0.49999999999999994
