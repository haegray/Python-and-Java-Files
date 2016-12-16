import random

def main():

    guessBag = 0

    print('Hello! What is your name?')
    myName = input()

    number = random.randint(1, 20)
    print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

    while guessBag < 6:
        print('What number am I thinking of?') # There are four spaces in front of print.
        guess = input()
        guess = int(guess)

        guessBag = guessBag + 1

        if guess < number:
            print('Your guess is too low.') # There are eight spaces in front of print.

        if guess > number:
            print('Your guess is too high.')

        if guess == number:
            break

    if guess == number:
        guessBag = str(guessBag)
        print('Good job, ' + myName + '! You guessed my number in ' + guessBag + ' guesses!')

    if guess != number:
        number = str(number)
        print('You have failed. The number I was thinking of was ' + number)
    main()
