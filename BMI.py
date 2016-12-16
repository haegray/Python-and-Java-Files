#BMI.py

def main():

    print("To calculate your BMI and assess your health your height and weight will be needed.")
    height = eval(input("Please enter your height in inches: "))
    weight = eval(input("Please enter your weight input pounds:"))
    bmi = (weight*703)/(height*height)

    if bmi <= 18.5:
        print('Your BMI is', bmi,'which means you are underweight.')

    elif bmi > 18.5 and bmi < 25:
        print('Your BMI is', bmi,'which means you are normal.')

    elif bmi > 25 and bmi < 30:
        print('Your BMI is', bmi,'which means you are overweight')

    elif bmi > 30:
        print('Your BMI is', bmi,'which means you are obese.')

    else:
        print('There is an error with you inputput')
        print('Please check you have entered whole numbers\n'
              'and decimals where asked.')
main()

#IOP:
#To calculate your BMI and assess your health your height and weight will be needed.
#Please enter your height in inches: 56
#Please enter your weight input pounds:118
#Your BMI is 26.45216836734694 which means you are overweight
#>>> main()
#To calculate your BMI and assess your health your height and weight will be needed.
#Please enter your height in inches: 68
#Please enter your weight input pounds:118
#Your BMI is 17.939878892733564 which means you are underweight.
#>>> main()
#To calculate your BMI and assess your health your height and weight will be needed.
#Please enter your height in inches: 57
#Please enter your weight input pounds:130
#Your BMI is 28.128654970760234 which means you are overweight
#>>> main()
#To calculate your BMI and assess your health your height and weight will be needed.
#Please enter your height in inches: 67
#Please enter your weight input pounds:130
#Your BMI is 20.35865448875028 which means you are normal.
