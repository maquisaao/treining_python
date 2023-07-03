import random
import time


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != '=':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(
            f'O numero {guess} é maior (+), menor (-), or igual (=)?? ').lower()
        if feedback == '+':
            high = guess - 1
        elif feedback == '-':
            low = guess + 1

    print(f'Issaaa! O programa adivinhou seu numero, {guess}, corretamente!')


time.sleep(5)

computer_guess(10)
