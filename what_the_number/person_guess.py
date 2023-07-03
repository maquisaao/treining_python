import random
import time


def guess(x):
    random_number = random.randint(1, 100)
    guess = 0
    while guess != random_number:
        guess = int(
            input(f'Adivinha o numero que estou pensando, de 1 a {x}: '))
        if guess < random_number:
            print('Que pena, tenta de novo. Muito baixo.')
        elif guess > random_number:
            print('Que pena, tenta de novo. Muito alto.')

    print(
        f'Isssaa! Parabens. Você acertou o numero que eu estava pensando, é o {random_number} !!')  # noqa: E501
    time.sleep(5)


guess(100)
