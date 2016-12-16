#leapyear.py

def main():

    print("To find out if a year is a leap year I will need to know what year.")
    year = eval(input("Type a year: ")) 

    if year%4 == 0 and year%100 != 0 or year%400 == 0:
            print ("It is a leap-year.")
    else:
            print ("It's not a leap-year.")

main()

#IOP:
#To find out if a year is a leap year I will need to know what year.
#Type a year: 1972
#It is a leap-year.
#>>> main()
#To find out if a year is a leap year I will need to know what year.
#Type a year: 2000
#It is a leap-year.
#>>> main()
#To find out if a year is a leap year I will need to know what year.
#Type a year: 2001
#It's not a leap-year.
#>>> 
