

def main():
    num = input('What is the numerical value of the month on the calendar? ')
    month = 'JanFebMarAprMayJunJulAugSepOctNowDec'
    month = [(num-1)*3:num*3]

    print(month)

main()
