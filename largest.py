#largest.py

def main():
        a,b,c= eval(input("Please input 3 numbers you would like to know the largest of: "))
        Max=a
        if c>Max:
            Max=c
        if b>Max:
            Max=b
        print("The largest number is " + str(Max) )
main()
        
