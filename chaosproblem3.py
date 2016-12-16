# File: chaos.py
#A simple program illustrating chaotic behavior.

def main():
    print("This program illustrates a chaotic function")
    x= eval(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 2.0 * x * (1-x)
        print(x)

main()

#This program illustrates a chaotic function
#Enter a number between 0 and 1: .7
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
