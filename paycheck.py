#paycheck.py

def main():
    print("To find the amount you will be paid this week, I need to know your hourly wage and hours you have worked.")
    hours = eval(input("Please enter the amount of hours you worked: "))
    wage = eval(input("Please enter your hourly wage: "))
    pay = (hours*wage)
    pass
    if hours > 40:
        pay = (40 * wage) + ((hours - 40) * 1.5 * (wage))
        print('You earned', pay)
    elif hours <= 40:
        print ('You earned', pay)

main()

#IOP:        
#>>> ================================ RESTART ================================
#>>> 
#To find the amount you will be paid this week, I need to know your hourly wage and hours you have worked.
#Please enter the amount of hours you worked: 50
#Please enter your hourly wage: 8.00
#You earned 440.0
#>>> 
#To find the amount you will be paid this week, I need to know your hourly wage and hours you have worked.
#Please enter the amount of hours you worked: 40
#Please enter your hourly wage: 8.00
#You earned 320.0
