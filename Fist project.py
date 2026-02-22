import time
import random

Guess_number = int(input("Guess a guessed number:"))

Secret_number = random.randint(1, 100)

if Guess_number == Secret_number:
    print('U guessed right!')
else:
    while Guess_number != Secret_number:
        More_attempt = int(input('Once more attempt: '))
        if More_attempt > 100:
            raise ValueError ('u daun, the numer have to be mote that 100')
        if More_attempt < 1:
            raise ValueError('u daun, the numer have to be mote that 100')

time.sleep(30)
print(f'OK, it\'s very hard for u, the secret number equall =:{Secret_number}')

